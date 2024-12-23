#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 熊🐻来个🥬
# @Date:  2024/12/22
# @Description: [对文件功能等的简要描述（可自行添加）]
# 字符串操作	统计查找替换类，字符串判断类，字符串转换类，字符串对齐类，字符串去除空白类，字符串分割类，字符串连接类，编码解码类，切片操作
# 字符串综合实战	字符串操作
# 字符串格式化	什么是字符串格式化，format()方法，f-string字符串

# 我们来详细讲解 Python 中的字符串操作，包括统计查找替换、判断、转换、对齐、去除空白、分割、连接、编码解码、切片以及字符串格式化。
# **课程模：Python 字符串操作详解**
# **第一部分：字符串基本概念**
# 字符串是由字符组成的不可变序列。可以使用单引号 `'`、双引号 `"` 或三引号 `'''` 或 `"""` 来创建字符串。
s1 = 'hello'
s2 = "world"
s3 = '''this is a
multiline string'''


# **第二部分：字符串操作**
# *   **统计查找替换类：**
#     *   `len(string)`：返回字符串的长度。
#     *   `string.count(substring)`：返回子字符串在字符串中出现的次数。
#     *   `string.find(substring)`：返回子字符串在字符串中首次出现的索引，如果不存在则返回 -1。
#     *   `string.rfind(substring)`：返回子字符串在字符串中最后一次出现的索引，如果不存在则返回 -1。
#     *   `string.index(substring)`：返回子字符串在字符串中首次出现的索引，如果不存在则抛出 `ValueError` 异常。
#     *   `string.rindex(substring)`：返回子字符串在字符串中最后一次出现的索引，如果不存在则抛出 `ValueError` 异常。
#     *   `string.replace(old, new, count)`：将字符串中的 `old` 子字符串替换为 `new` 子字符串，`count` 指定替换的次数，默认为全部替换。

s = "hello world hello"
print(len(s))        # 输出：17
print(s.count("hello")) # 输出：2
print(s.find("world")) # 输出：6
print(s.replace("hello", "hi")) # 输出：hi world hi


# *   **字符串判断类：**
#     *   `string.startswith(prefix)`：判断字符串是否以指定的前缀开头。
#     *   `string.endswith(suffix)`：判断字符串是否以指定的后缀结尾。
#     *   `string.isalnum()`：判断字符串是否只包含字母和数字。
#     *   `string.isalpha()`：判断字符串是否只包含字母。
#     *   `string.isdigit()`：判断字符串是否只包含数字。
#     *   `string.isspace()`：判断字符串是否只包含空白字符。
#     *   `string.islower()`：判断字符串是否所有字母都是小写。
#     *   `string.isupper()`：判断字符串是否所有字母都是大写。

s = "HelloWorld"
print(s.startswith("Hello")) # 输出：True
print(s.isupper()) # 输出：False


# *   **字符串转换类：**
#     *   `string.lower()`：将字符串转换为小写。
#     *   `string.upper()`：将字符串转换为大写。
#     *   `string.capitalize()`：将字符串的第一个字符转换为大写，其余字符转换为小写。
#     *   `string.title()`：将字符串中每个单词的首字母转换为大写。
#     *   `str(object)`：将其他类型的对象转换为字符串。
s = "hello world"
print(s.upper()) # 输出：HELLO WORLD


# *   **字符串对齐类：**
#     *   `string.ljust(width, fillchar)`：将字符串左对齐，并使用 `fillchar` 填充到指定宽度。
#     *   `string.rjust(width, fillchar)`：将字符串右对齐，并使用 `fillchar` 填充到指定宽度。
#     *   `string.center(width, fillchar)`：将字符串居中对齐，并使用 `fillchar` 填充到指定宽度。
s = "hello"
print(s.ljust(10, '*')) # 输出：hello*****


# *   **字符串去除空白类：**
#     *   `string.strip()`：去除字符串开头和结尾的空白字符。
#     *   `string.lstrip()`：去除字符串开头的空白字符。
#     *   `string.rstrip()`：去除字符串结尾的空白字符。
s = "   hello world   "
print(s.strip()) # 输出：hello world


# *   **字符串分割类：**
#     *   `string.split(sep, maxsplit)`：使用指定的分隔符 `sep` 将字符串分割成一个列表，`maxsplit` 指定最大分割次数。
#     *   `string.rsplit(sep, maxsplit)`：从右侧开始分割。
#     *   `string.partition(sep)`：从左侧找到第一个分隔符 `sep`，将字符串分割成一个包含三个元素的元组 `(分隔符左侧的字符串, 分隔符, 分隔符右侧的字符串)`。
#     *   `string.rpartition(sep)`：从右侧开始分割。
s = "hello,world,python"
print(s.split(",")) # 输出：['hello', 'world', 'python']


# *   **字符串连接类：**
#     *   `string.join(iterable)`：使用字符串将可迭代对象（如列表、元组）中的元素连接成一个字符串。
words = ["hello", "world", "python"]
print(",".join(words)) # 输出：hello,world,python

# *   **编码解码类：**
#     *   `string.encode(encoding)`：使用指定的编码格式将字符串编码成字节串。
#     *   `bytes.decode(encoding)`：使用指定的编码格式将字节串解码成字符串。
s = "你好"
encoded_s = s.encode("utf-8")
decoded_s = encoded_s.decode("utf-8")
print(encoded_s)
print(decoded_s)


# *   **切片操作：**
#     可以使用切片操作 `[start:stop:step]` 来访问字符串的部分内容。
s = "hello world"
print(s[0:5])   # 输出：hello
print(s[6:])    # 输出：world
print(s[::2])   # 输出：hlowrd
print(s[::-1])  # 输出：dlrow olleh


# **第三部分：字符串格式化**
# 字符串格式化用于将变量的值插入到字符串中。Python 提供了多种字符串格式化方法。
#
# *   **什么是字符串格式化：**
#     字符串格式化就是将不同的变量值插入到字符串中，生成新的字符串。
#
# *   **`format()` 方法：**
#     `str.format()` 方法使用花括号 `{}` 作为占位符，可以使用位置参数或关键字参数来指定要插入的值。

name = "Alice"
age = 30
print("My name is {} and I am {} years old.".format(name, age))  # 输出：My name is Alice and I am 30 years old.
print("My name is {1} and I am {0} years old.".format(age, name)) # 输出：My name is Alice and I am 30 years old.
print("My name is {name} and I am {age} years old.".format(name=name, age=age)) # 输出：My name is Alice and I am 30 years old.


# *   **f-string 字符串（Python 3.6+）：**
# f-string 是 Python 3.6 引入的一种新的字符串格式化方法，使用 `f` 或 `F` 前缀，可以直接在字符串中使用变量名。

name = "Bob"
age = 25
print(f"My name is {name} and I am {age} years old.")  # 输出：My name is Bob and I am 25 years old.


# f-string 还支持在花括号中使用表达式：
x = 10
y = 5
print(f"The sum of {x} and {y} is {x + y}.")  # 输出：The sum of 10 and 5 is 15.


# **第四部分：字符串综合实战**
# 通过一些实际的例子来综合运用所学的字符串操作技巧，例如：
# *   提取 URL 中的域名。
# *   验证用户输入的邮箱地址是否合法。
# *   统计文章中单词出现的频率。
# *   格式化输出表格数据。
