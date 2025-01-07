#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 熊🐻来个🥬
# @Date:  2024/12/25
# @Description: [对文件功能等的简要描述（可自行添加）]

# Python 匹配语句match和循环语句及实战【回文数，数字序列，猜数字】
'''
1. 匹配语句 (match)
1.1 匹配语句 match 介绍
match 是 Python 3.10 引入的一种新的结构化模式匹配语句，它类似于其他语言中的 switch 或 case 语句，但提供了更强大和灵活的功能，支持通过模式匹配来解构和匹配复杂的数据结构。
1.2 基本语法结构
match 语句的基本结构如下：
def match_example(value):
    match value:
        case 1:
            print("匹配 1")
        case 2:
            print("匹配 2")
        case _:
            print("没有匹配")
- match 后接待匹配的值。
- 每个 case 后面跟一个匹配条件，匹配成功时执行对应的代码块。
- _ 是默认的匹配模式，类似于 else，匹配所有其他情况。
1.3 组合多个匹配值
可以在一个 case 中匹配多个值。只需将它们用竖线 | 分隔开：
def match_example(value):
    value = 404
    match value:
        case 400:
            print("Bad request")
        case 401 | 403 | 404:  匹配 401、403 或 404
            print("Not allowed")
        case 500:
            print("Internal server error")
        case _:
            print("Unknown status")
1.4 匹配模式绑定变量
可以将匹配到的值绑定到变量上，这样在后续的代码中可以使用这些变量：
def match_example(value):
    match value:
        case (x, y):
            print(f"匹配元组，x = {x}, y = {y}")
        case [x, y]:
            print(f"匹配列表，x = {x}, y = {y}")
        case _:
            print("没有匹配")
如果 value 是一个元组 (1, 2)，那么 x 和 y 会分别绑定到 1 和 2。
2. 循环语句 (while)
2.1 什么是循环
循环是程序中重复执行某些操作的一种控制结构，通常用于处理需要重复执行的任务。
2.2 程序中的循环
循环语句使得程序能够在满足特定条件下重复执行某些代码，直到条件不再满足。
2.3 循环的作用
- 重复执行一段代码。
- 节省代码重复量。
- 根据不同的输入或条件动态控制执行次数。
2.4 循环的构成要素
- 初始化：设置循环控制变量。
- 条件判断：控制循环是否继续执行。
- 更新：更新循环控制变量，防止无限循环。
2.5 while 循环的语法
while 循环会在条件为 True 时反复执行代码块。
count = 0
while count < 5:
    print(count)
    count += 1
- 先判断 count < 5 是否为 True，如果是，则执行循环体内的代码，并更新 count。直到条件为 False 时，跳出循环。
2.6 while 循环实战
模拟用户输入密码，直到用户输入正确为止：
password = "1234"
input_password = ""
while input_password != password:
    input_password = input("请输入密码：")
    if input_password != password:
        print("密码错误，请重试。")
print("密码正确，登录成功！")
3. 循环语句 (for-in)
3.1 for-in 循环的语法
for 循环常用于遍历可迭代对象（如列表、元组、字典等）。基本语法如下：
for item in iterable:
    # 执行代码块
3.2 遍历可迭代对象
for 循环能够遍历列表、字符串、字典、集合等可迭代对象。
遍历列表
my_list = [1, 2, 3, 4]
for num in my_list:
    print(num)
遍历字符串
for char in "Hello":
    print(char)
4. 回文数（循环实现）
4.1 类型转换
将数字转换为字符串，使用循环逐位比较判断是否为回文数。
4.2 运算符
使用运算符进行条件判断和对数字进行操作。
4.3 循环语句 (for-in)
通过循环逐位比较一个数字的正向和反向。
def is_palindrome(n):
    num_str = str(n)
    length = len(num_str)
    for i in range(length // 2):
        if num_str[i] != num_str[length - i - 1]:
            return False
    return True
num = 121
if is_palindrome(num):
    print(f"{num} 是回文数")
else:
    print(f"{num} 不是回文数")
5. 数字序列 (range 函数)
5.1 range 函数
range 函数返回一个可迭代对象，表示一个整数序列，常用于循环中。
- 基本语法：range(start, stop, step)
  - start：起始值（默认为 0）
  - stop：结束值（不包含该值）
  - step：步长（默认为 1）
for i in range(5):
    print(i)  # 输出：0 1 2 3 4
5.2 range 函数的基本语法
for i in range(1, 10, 2):
    print(i)  # 输出：1 3 5 7 9
5.3 随机数
Python的 random 模块可以生成随机数。
import random
print(random.randint(1, 100))  # 输出一个1到100之间的随机整数
6. 猜数字
6.1 循环语句 (while)
用户需要猜测一个数字，直到猜中为止：
import random
secret_number = random.randint(1, 100)
guess = None
while guess != secret_number:
    guess = int(input("请输入你猜的数字："))
    if guess < secret_number:
        print("猜小了")
    elif guess > secret_number:
        print("猜大了")
    else:
        print("恭喜你，猜对了！")
6.2 循环语句 (for-in)
可以使用 for-in 循环来限制猜数字的次数，例如限制用户最多猜 10 次：
import random
secret_number = random.randint(1, 100)
for _ in range(10):
    guess = int(input("请输入你猜的数字："))
    if guess < secret_number:
        print("猜小了")
    elif guess > secret_number:
        print("猜大了")
    else:
        print("恭喜你，猜对了！")
        break
else:
    print("很遗憾，你没有猜对，正确答案是", secret_number)

'''