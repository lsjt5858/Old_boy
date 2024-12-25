#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 熊🐻来个🥬
# @Date:  2024/12/25
# @Description: [对文件功能等的简要描述（可自行添加）]

# Python 分支语句
'''
1. 分支语句
1.1 什么是分支语句
分支语句（Conditional Statements）用于控制程序的流程，根据条件判断不同的路径。Python中的分支语句包括 if 语句、if...else 语句、if...elif...else 语句等。
1.2 if 条件判断
if 语句用于判断一个条件是否成立，若条件成立，则执行相应的代码块；否则，跳过该代码块。
age = 18
if age >= 18:
    print("成年")
1.3 if... else 判断语句
if...else 语句用于判断一个条件是否成立，如果条件成立，执行 if 代码块，否则执行 else 代码块。
age = 16
if age >= 18:
    print("成年")
else:
    print("未成年")
1.4 if... elif... else 多重条件
if...elif...else 语句用于处理多个条件的判断。elif 用于添加额外的条件判断，else 用于处理所有条件不成立的情况。
age = 20
if age < 13:
    print("儿童")
elif 13 <= age < 18:
    print("青少年")
else:
    print("成人")
1.5 分支嵌套
可以将一个 if 语句嵌套在另一个 if 语句中，这样可以处理更复杂的条件。
age = 25
has_ticket = True
if age >= 18:
    if has_ticket:
        print("允许进入")
    else:
        print("没有票，不能进入")
else:
    print("未成年，不能进入")
2. 回文数（切片实现）
回文数是指正着读和反着读都一样的数。例如：121 是回文数，-121 不是回文数。
2.1 运算符
运算符用于执行数学运算或比较。常见的运算符有：
- 算术运算符：+, -, *, /, %
- 比较运算符：==, !=, <, >, <=, >=
- 逻辑运算符：and, or, not
2.2 分支语句 - if
通过 if 判断一个数是否为回文数。
2.3 字符串操作 - 切片
利用字符串切片功能来判断一个数是否为回文数。将数字转换为字符串，反转字符串并进行比较。
def is_palindrome(n):
    n_str = str(n)
    if n_str == n_str[::-1]:  # 切片反转字符串
        return True
    return False
num = 121
if is_palindrome(num):
    print(f"{num} 是回文数")
else:
    print(f"{num} 不是回文数")
3. 成绩判断
根据成绩输出相应的等级。
3.1 类型转换
通过 int() 或 float() 函数将输入的字符串转换为数字类型。
score = input("请输入成绩：")
score = float(score)  # 类型转换为浮点数
3.2 分支语句 - if
使用 if 判断成绩的范围，并给出不同的输出。
score = float(input("请输入成绩："))
if score >= 90:
    print("优秀")
elif score >= 70:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")
4. 计算器
实现一个简单的计算器，可以进行加减乘除运算。
4.1 类型转换
输入的数字是字符串类型，使用 float() 转换为浮动数字类型。
4.2 运算符
通过输入的运算符来进行加减乘除的运算。
4.3 分支语句 - if
通过 if...elif...else 判断运算符，并执行对应的运算。
num1 = float(input("请输入第一个数字："))
operator = input("请输入运算符 (+, -, *, /)：")
num2 = float(input("请输入第二个数字："))
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "不能除以零"
else:
    result = "无效运算符"
print(f"结果是: {result}")
5. 模拟乘车过程
模拟一个简单的乘车过程，检查乘客是否满足乘车条件。
5.1 分支语句 - if
通过 if 判断乘客的年龄和是否有车票，决定是否允许乘车。
age = int(input("请输入您的年龄："))
has_ticket = input("您是否有车票？(yes/no): ").lower()
if age >= 18 and has_ticket == "yes":
    print("您可以乘车")
else:
    print("您不能乘车")


'''