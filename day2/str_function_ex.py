#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
str类的内建方法练习

"""
name1 = 'alex'
name2 = str('ERIC')  # 调用字符串类的__init__()方法
print(type(name1))
print(dir(name1))  # 打印出类的成员

# 包含
result = name1.__contains__('ex')
print(result)
result = 'ex' in name1
print(result)

# 等于
print(name1.__eq__(name2))

# 字符串按照format_spec格式化
"""
 format_spec ::=  [[fill]align][sign][#][0][width][,][.precision][type]

fill        ::=  <any character>

align       ::=  "<" | ">" | "=" | "^"

sign        ::=  "+" | "-" | " "

width       ::=  integer

precision   ::=  integer

type        ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"

fill是表示可以填写任何字符。

align是对齐方式，<是左对齐， >是右对齐，^是居中对齐。

sign是符号， +表示正号， -表示负号。

width是数字宽度，表示总共输出多少位数字。

precision是小数保留位数。

type是输出数字值是的表示方式，比如b是二进制表示；比如E是指数表示；比如X是十六进制表示。
"""
# 共20个字符，name1右对齐
print(name1.__format__('>20'))

# 返回小写
result = name2.casefold()
print(result)

# 居中
# print('*' * 8 %s '*' * 8 % name1)
result = name1.center(20, '*')
print(result)

# 获取指定标签属性的值
print(name1.__getattribute__('index'))

# x.__getitem__(y) <==> x[y](返回str[key])
print(name1.__getitem__(1))

# 大于等于
print(name1.__ge__(name2))

# 大于
print(name1.__gt__(name2))

# 哈希
print(name1.__hash__())

# 返回一个字符串的迭代
for i in name1.__iter__():
    print(i)

# 返回字符串的长度
print(name1.__len__())

# 首字母大写
print(name1.capitalize())

# 返回将小写字符串转换为大写，大写转换为小写
name3 = "AlEx"
print(name1.swapcase())
print(name2.swapcase())
print(name3.swapcase())

# 返回str的小写
print(name2.casefold())

# 将字符串转换为标题：每个单词的首字母大写
str_temp = "eric is humor!"
print(str_temp.title())

# 居中 下例为：20个字符的宽度以'*'号填充，name1居中
print(name1.center(20, '*'))

# count 计数
str1 = 'adasafafdsfqadasddfa'
result = str1.count('a')
print(result)

# encode 编码
result = name1.encode('gbk')
print(result)

# endswith 以'xxx'结束，后面可跟索引
result = str1.endswith('a')
print(result)
result = str1.endswith('s', 2, 4)
print(result)

# 替换tabs tabsize默认为8
name_temp = 'a\nlex'
print(name_temp.expandtabs())
print(len(name_temp.expandtabs()))

# 查找 返回索引值
print(name1.find('e'))

# 格式化
str_temp = '{} is humor!'
print(str_temp.format(name2))

# 按映射格式化
# format_map(self, mapping)

# 返回索引值 index(self, sub, start=None, end=None) 没有返回0
print(name1.index('l'))

str_temp = 'a1b2c3'
# 判断字符串是否是字母或数字
print(str_temp.isalnum())

# 判断字符串是否只是字母
print(str_temp.isalpha())

# 判断字符串中是否只包含十进制字符
str_temp = '0.3a0.4b'
str_temp1 = '0.3'
print(str_temp.isdecimal())
print(str_temp1.isdecimal())

# 判断字符串中是否只有数字
str_temp = b'12345'
str_temp1 = '12345'
str_temp2 = '四'
print(str_temp.isdigit())
print(str_temp1.isdigit())
print(str_temp2.isdigit())

print("line:148".center(20, "="))

# 判断是否是标识符
str_temp = 'class'
print(str_temp.isidentifier())

# 判断字符串中是否都是小写
str_temp = 'eric'
str_temp1 = 'Eric'
print(str_temp.islower())
print(str_temp1.islower())

# 判断字符串中是否都是数值型字符串
# 'bytes' object has no attribute 'isnumeric'
str_temp = '12345'
str_temp1 = '12345'
str_temp2 = '四'
str_temp3 = '壹佰贰拾叁'
print(str_temp.isnumeric())
print(str_temp1.isnumeric())
print(str_temp2.isnumeric())
print(str_temp3.isnumeric())

# 判断是否可被打印
str_temp = 'abc'
print(str_temp.isprintable())

# 是否为空格
str_temp = ' '
print(str_temp.isspace())

# 判断是否为标题 （所有首字母大写）
str_temp = 'eric is humor!'
str_temp1 = 'Eric Is Humor!'
print(str_temp.istitle())
print(str_temp1.istitle())

print('line:185'.center(20, '='))

# 判断字符串是否全为大写
str_temp = 'eric is humor!'
str_temp1 = 'Eric Is Humor!'
str_temp2 = 'ERIC IS HUMOR!'
print(str_temp.isupper())
print(str_temp1.isupper())
print(str_temp2.isupper())

# 字符串的拼接 join(self, iterable)
str_temp = "ERIC"
print(':'.join(str_temp))

# 左对齐
str_temp = "eric"
print(str_temp.ljust(20, '*'))
# 右对齐
print(str_temp.rjust(20, '*'))

# 将字符串转换为小写
str_temp = "ERIC"
print(str_temp.lower())
# 将字符串转换为大写
str_temp1 = "eric"
print(str_temp1.upper())

# strip()移除字符串前后的指定字符；lstrip()移除左边指定字符 默认为移除空格;rstrip()移除右边指定字符
str_temp = "   eric is humor   !   "
print(str_temp.strip())
print(str_temp.lstrip())
print(str_temp.rstrip())
str_temp1 = "eric is humor!"
print(str_temp1.lstrip('eric'))
print(str_temp1.rstrip('mor!'))

# maketrans(self, *args, **kwargs)和translate()
str_temp = '654321123789'
map_temp = str.maketrans('123', 'abc')
map_temp1 = str.maketrans('123', 'abc', '789')
print(str_temp.translate(map_temp))
print(str_temp.translate(map_temp1))

# 按照指定分隔符将字符串分割，返回元祖
# 如果字符串包含指定的分隔符，则返回一个三元的元组，第一个为分隔符左边的子串，第二个为分隔符本身，第三个为分隔符右边的子串。
# 如果字符串不包含指定的分隔符，则返回一个三元的元祖，第一个为字符串本身，第二个、第三个为空字符串。
str_temp = "www.google.com"
print(str_temp.partition('google'))
print(str_temp.partition('www'))
print(str_temp.partition('wxw'))

# 右侧开始分隔
print(str_temp.partition('o'))
print(str_temp.rpartition('o'))

# Python replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。
str_temp = "www.google.com"
print(str_temp.replace('.', '-', 1))

# 右查找
str_temp.rfind('.')

# 右索引
str_temp.rindex('.')

# 分割
str_temp = "www.google.com"
print(str_temp.split('o', 2))
# 右分隔
print(str_temp.rsplit('o', 2))

print('line:252'.center(20, '='))

# 行分割
str_temp = """
eric
is
humor
!
"""
print(str_temp.splitlines())

# 以什么开始
str_temp = "eric is humor!"
print(str_temp.startswith('eric'))

# 返回指定长度的字符串，原字符串右对齐，前面补0
str_temp = "23"
print(str_temp.zfill(20))
