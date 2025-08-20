# 获取接口数据
"""
# 获取 rankingId
curl 'https://editor.guiderank-app.com/guiderank-editor/admin/car/getCarRankings?token=lm11ePrQZd9ywZezee2hP9fJ' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: zh-CN,zh;q=0.9,en;q=0.8' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'DNT: 1' \
  -H 'Origin: https://editor.guiderank-app.com' \
  -H 'Referer: https://editor.guiderank-app.com/guiderank-admin/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  --data-raw '{"firstCategoryId":"","secondCategoryId":"","name":""}'

# 获取榜单信息
  curl 'https://editor.guiderank-app.com/guiderank-editor/admin/car/getCarRankingGlobals?token=lm11ePrQZd9ywZezee2hP9fJ' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: zh-CN,zh;q=0.9,en;q=0.8' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'DNT: 1' \
  -H 'Origin: https://editor.guiderank-app.com' \
  -H 'Referer: https://editor.guiderank-app.com/guiderank-admin/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  --data-raw '{"rankingId":"15601363360420320766"}'

"""

import requests

# 定义请求头
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'DNT': '1',
    'Origin': 'https://editor.guiderank-app.com',
    'Referer': 'https://editor.guiderank-app.com/guiderank-admin/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"'
}

# 获取榜单明细数据
def get_ranking(rankingId, rankingName, headers):
    url = 'https://editor.guiderank-app.com/guiderank-editor/admin/car/getCarRankingGlobals?token=lm11ePrQZd9ywZezee2hP9fJ'
    data = {
        "rankingId": rankingId
    }

    response = requests.post(url, headers=headers, json=data)
    result = response.json()

    print(rankingName + "排行榜")
    for item in result['data']['globals']:
        print("   " + str(item['seq']) + "." + item['carSeriesName'] + " 评分：" + str(item['score']))


# 获取rankingId
url = "https://editor.guiderank-app.com/guiderank-editor/admin/car/getCarRankings?token=lm11ePrQZd9ywZezee2hP9fJ"
data = {
    "firstCategoryId":"",
    "secondCategoryId":"",
    "name":""
}

response = requests.post(url, json=data, headers=headers)
result = response.json()
print(result)

    rankingId = item['rankingId']
    get_ranking(rankingId, rankingName, headers)
