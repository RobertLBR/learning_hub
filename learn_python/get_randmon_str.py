# 生成随机密码
import random

# 把所有数字放去列表
pwd_list = [str(i) for i in range(10)]

# 把所有大小写字母放去列表
for i in range(97, 123):
    pwd_list.append(chr(i))
    pwd_list.append(chr(i).upper())

# 列表转字符串
str_list = ''.join(pwd_list)

# 字符串合并
pwd_str= str_list + "!@#$%^&*())_+<>?,./`-"

# 随机打印出16个字符作为密码
bits = 16
random_str = random.sample(pwd_str, bits)
print(''.join(random_str))

