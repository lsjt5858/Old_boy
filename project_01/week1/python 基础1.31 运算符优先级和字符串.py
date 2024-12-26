#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 熊🐻来个🥬
# @Date:  2024/12/25
# @Description: [对文件功能等的简要描述（可自行添加）]

'''
我们来详细讲解运算符优先级规则、括号、字符串的定义、转义字符以及字符串下标。
课程模块：Python 运算符、字符串详解
目标： 使学员全面掌握 Python 中运算符的优先级、字符串的各种特性和操作。
时长： 半天
第一部分：运算符优先级规则
Python 中运算符的优先级决定了表达式中运算的执行顺序。优先级高的运算符先执行，优先级低的运算符后执行。可以使用括号 () 来改变运算的执行顺序。
以下是 Python 中运算符的优先级顺序（从高到低）：
1. 括号 ()： 括号具有最高的优先级，可以改变运算的执行顺序。
2. 指数 **： 指数运算的优先级高于乘除和取余。
3. 正负号 +、-： 一元正负号。
4. 乘法 *、除法 /、整除 //、取余 %： 乘除和取余的优先级相同，从左到右依次计算。
5. 加法 +、减法 -： 加减法的优先级相同，从左到右依次计算。
6. 位运算符 <<、>>、&、^、|： 位运算。
7. 比较运算符 >、<、>=、<=、==、!=： 比较运算。
8. 逻辑运算符 not、and、or： 逻辑运算，not 的优先级最高，然后是 and，最后是 or。
9. 赋值运算符 =、+=、-=、*=、/=、//=、%=、&=、|=、^=、>>=、<<=： 赋值运算。
示例：
result1 = 2 + 3 * 4  先计算 3 * 4，然后加上 2，结果为 14
result2 = (2 + 3) * 4  先计算 2 + 3，然后乘以 4，结果为 20
result3 = 2 ** 3 * 2 先计算 2**3 = 8, 然后计算 8 * 2 = 16
print(f"result1: {result1}")
print(f"result2: {result2}")
print(f"result3: {result3}")
x = 5
x += 3 x = x + 3
print(x) 输出 8
第二部分：括号 ()
括号 () 在 Python 中有多种用途：
- 改变运算的执行顺序： 如上例所示。
- 函数调用： 例如 print(), len(), str() 等。
- 元组的定义： 例如 (1, 2, 3)。
- 生成器表达式： 例如 (x**2 for x in range(10))。
第三部分：字符串
- 字符串定义：字符串是由字符组成的不可变序列。可以使用单引号 '、双引号 " 或三引号 \''' 或 """ 来定义字符串。
str1 = 'hello'
str2 = "world"
str3 = \'''This is a
multi-line string\'''
str4 = """This is another
multi-line string"""
- 转义字符：
- 转义字符用于表示一些特殊的字符，例如换行符、制表符等。
  - \n：换行符。
  - \t：制表符。
  - \'：单引号。
  - \"：双引号。
  - \\：反斜杠。
print("Hello\nWorld")  输出：Hello (换行) World
print("This is a \"quoted\" string")  输出：This is a "quoted" string
print("This is a backslash: \\") 输出 This is a backslash: \
- 字符串下标（索引）：
- 可以使用下标（索引）来访问字符串中的单个字符。索引从 0 开始，负数索引表示从字符串末尾开始计数。
s = "Python"
print(s[0])   输出：P
print(s[1])   输出：y
print(s[-1])  输出：n
print(s[-2])  输出：o
- 字符串切片：
- 可以使用切片来获取字符串的子串。
s = "Python"
print(s[1:4])   输出：yth (从索引 1 到 3 的字符)
print(s[:3])    输出：Pyt (从索引 0 到 2 的字符)
print(s[2:])    输出：thon (从索引 2 到末尾的字符)
print(s[:])     输出：Python (复制整个字符串)
print(s[::2])  输出：Pto (每隔一个字符取一个)
print(s[::-1]) 输出：nohtyP (反转字符串)
- 字符串的常用操作：
  - len(s)：返回字符串的长度。
  - s.lower()：将字符串转换为小写。
  - s.upper()：将字符串转换为大写。
  - s.strip()：去除字符串两端的空白字符。
  - s.split(sep)：使用指定的分隔符 sep 分割字符串，返回一个列表。
  - sep.join(list)：使用指定的分隔符 sep 将列表中的字符串连接成一个字符串。
  - s.replace(old, new)：将字符串中的 old 子串替换为 new 子串。
  - s.find(sub)：查找子串 sub 在字符串中首次出现的索引，如果找不到则返回 -1。
  - s.startswith(prefix)：判断字符串是否以指定的前缀 prefix 开头。
  - s.endswith(suffix)：判断字符串是否以指定的后缀 suffix 结尾。
  - f-string (格式化字符串字面值)：使用 f 前缀的字符串，可以在字符串中嵌入表达式。
s = "  Hello, World!  "
print(len(s)) 输出 17
print(s.lower()) 输出 "  hello, world!  "
print(s.strip()) 输出 "Hello, World!"
words = s.split(",")
print(words) 输出 ['  Hello', ' World!  ']
print("-".join(words)) 输出 '  Hello- World!  '
print(s.replace("World", "Python")) 输出 '  Hello, Python!  '
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.") 输出 My name is Alice and I am 30 years old.
'''