# learning python
# test_str = "abcd"

# upper_test_str = test_str.upper()
# lower_test_str = upper_test_str.lower()

# # print(upper_test_str, lower_test_str)

# test_str = ".@#Python学习.@#"
# strip_test_str = test_str.strip('.@#')
# print(strip_test_str)

import re

url_str = "https://www.baidu.com"

results = re.findall("https://(.*?)",url_str)
for result in results:
    print(result)


# def is_valid_phone_number(phone_number):
#     # 中国大陆手机号码的正则表达式
#     pattern = r'^1[3-9]\d{9}$'
    
#     # 使用re.match()来检查字符串是否与正则表达式匹配
#     if re.match(pattern, phone_number):
#         return True
#     else:
#         return False

# # 测试一些手机号
# test_numbers = [
#     "13800138000",  # 有效手机号
#     "12345678901",  # 无效手机号（第二位不是3-9）
#     "1380013800",   # 无效手机号（长度不足11位）
#     "13800138000a", # 无效手机号（包含字母）
#     "+8613800138000" # 无效手机号（包含国际区号，尽管这个号码本身有效）
# ]

# for number in test_numbers:
#     if is_valid_phone_number(number):
#         print(f"{number} 是有效的手机号。")
#     else:
#         print(f"{number} 不是有效的手机号。")