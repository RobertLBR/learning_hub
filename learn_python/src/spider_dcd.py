import requests
import pandas as pd
import time
import logging
from datetime import datetime
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# 日志配置
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s: %(message)s',
    handlers=[logging.FileHandler('../car_crawler.log'), logging.StreamHandler()]
)


class DongCheDiCrawler:
    def __init__(self):
        self.base_url = "https://www.dongchedi.com/motor/car_page/m/v6/new_car_release"
        self.session = requests.Session()
        self._setup_session()
        self.result_df = pd.DataFrame()

    def _setup_session(self):
        """配置会话参数"""
        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET"]
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)

        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Referer": "https://www.dongchedi.com/newcar",
            "Accept-Encoding": "gzip, deflate, br"
        })

    def _generate_params(self, month, offset):
        """生成动态查询参数"""
        return {
            "aid": 1839,
            "app_name": "auto_web_pc",
            "category": -1,
            "month": month,  # 格式：YYYY0M，例如202504
            "offset": offset
        }

    def _parse_data(self, data):
        """解析嵌套JSON结构"""
        try:
            # 展开嵌套字段
            df = pd.json_normalize(
                data['data']['series_list'],
                meta=[
                    'series_id', 'series_name',
                    ['price_info', 'price'],
                    ['price_info', 'unit_text'],
                    'online_date_unix'
                ],
                errors='ignore'
            )

            # 重命名列
            df = df.rename(columns={
                'price_info.price': 'price_range',
                'price_info.unit_text': 'price_unit'
            })

            # 转换时间戳
            df['online_date'] = df['online_date_unix'].apply(
                lambda x: datetime.fromtimestamp(x).strftime('%Y-%m-%d') if x else None
            )

            return df[['series_id', 'series_name', 'price_range',
                       'price_unit', 'online_date', 'cover_url']]
        except KeyError as e:
            logging.error(f"JSON结构异常: {str(e)}")
            return pd.DataFrame()

    def _safe_request(self, params):
        """带异常处理的请求方法"""
        try:
            response = self.session.get(
                self.base_url,
                params=params,
                timeout=10
            )
            response.raise_for_status()

            if response.json().get('status') != 0:
                logging.warning(f"接口返回异常状态码: {response.json()}")
                return None

            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"请求失败: {str(e)}")
            return None

    def crawl(self, start_month=202504, max_pages=10):
        """执行爬取任务"""
        offset = 0
        current_month = start_month

        for _ in range(max_pages):
            params = self._generate_params(month=current_month, offset=offset)
            logging.info(f"正在抓取: {params}")

            data = self._safe_request(params)
            if not data:
                break

            page_df = self._parse_data(data)
            if page_df.empty:
                logging.info("没有更多数据")
                break

            self.result_df = pd.concat([self.result_df, page_df], ignore_index=True)

            # 动态分页控制
            if len(data['data']['series_list']) < 20:  # 假设每页20条
                current_month -= 1  # 切换到上月
                offset = 0
            else:
                offset += 20

            time.sleep(1.5)  # 遵守爬虫礼仪

    def save_data(self, filename="dongchedi_cars.csv"):
        """保存数据"""
        if not self.result_df.empty:
            self.result_df.to_csv(filename, index=False)
            logging.info(f"成功保存{len(self.result_df)}条数据到{filename}")
        else:
            logging.warning("没有数据需要保存")


if __name__ == "__main__":
    crawler = DongCheDiCrawler()
    crawler.crawl(start_month=202504, max_pages=50)
    crawler.save_data()
