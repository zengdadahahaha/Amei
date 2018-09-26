import re

it = re.finditer(r'\d+','2008-2018 10年,中国发生了翻天覆地的变化')


for i in it:
	print(i.group())

obj = re.fullmatch(r'\w+','abcde123')
# print(obj.group())

obj = re.match(r'foo','foodd')
print(obj.group())