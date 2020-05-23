import re
s  = "Alix:10,Bob:200"
pat = r"\w+:\d+"
regx = re.compile(pat)
result = regx.findall(s)
print(result)

print(dir(re))

ra = re.split(r"[:,]",s)
print(ra)

ra = re.sub(r":",r"-",s)
#返回字符串
print(ra)

ra = re.subn(r":",r"-",s)
print(ra)

x = "中观100,美国2000"
ra = re.fullmatch(r"[,\w]+",x).group()
print(ra)
print("=========================")
ra = re.finditer(r"\w+:\d+",s)
for i in ra:
    print(i.group())