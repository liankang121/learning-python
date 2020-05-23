# 匹配一个.com 邮箱字符串
#2. 匹配一个密码 8-12位 数字字母下划线构成
# 匹配一个数字 正数、负数、小数、分数、百分比
#匹配一段文字中以大写字母开头的文字，注意中间有大写的不算 单词中可能又大写字母 小写字母 -

import  re
# 匹配一个.com 邮箱字符串
res = re.findall(r"\b\w+@\w+\.com","df www.liankang@164.com")
print(res)
# 匹配一个密码 8-12位 数字字母下划线构成
res = re.findall(r"\w{8,12}","Tedu01234_")
print(res)

# 匹配一个数字,包含整数 小数  正数  负数  分数1/2 和百分数 4.6%
res = re.findall(r"-?\d+\.?\/?\d*%?","1 -21 12.5 -12.87 1/3 4.6%")
print(res)
# 匹配一段文字中以大写字母开头的单词,注意文字中可能含有 iPython 这种,不算大写字母开头, H-base这种算大写
#字母开头,  BSD 也是Hello iPython H-base BSD
res = re.findall(r"\b[A-Z]-?\w+","Hello iPython H-base BSD")
print(res)

res = re.search(r"\b\d{18}","15521232241 410823199410130111 helloworld").group()
print(res)
