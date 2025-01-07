#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 熊🐻来个🥬
# @Date:  2024/12/27
# @Description: [对文件功能等的简要描述（可自行添加）]

'''
try:
    num1 = int(input("请输入一个整数："))
    num2 = int(input("请输入另一个整数："))
    result = num1 / num2
    print(f"结果是：{result}")
except ZeroDivisionError:
    print("错误：除数不能为零！")
except ValueError:
    print("错误：请输入有效的整数！")
except Exception as e: 将异常信息存储在变量e中
    print(f"发生未知错误：{e}")
else:
    print("计算成功！")
finally:
    print("程序执行完毕。")

'''


# ======================计算机 的 异常处理 与逻辑==========================================
def calculate():
    while True:
        try:
            num1 = int(input("请输入一个整数："))
            operator = input("请输入运算符（+，-，*，/）: ")
            num2 = int(input("请输入另一个整数："))
            if operator == "+":
                result = num1 + num2
                print(f"结果是: {result}")
            elif operator == "-":
                result = num1 - num2
                print(f"结果是: {result}")
            elif operator == "*":
                result = num1 * num2
                print(f"结果是: {result}")
            elif operator == "/":
                if num2 == 0:
                    raise ZeroDivisionError("错误：除数不能为零！")
                result = num1 / num2
                print(f"结果是: {result}")
            else:
                print("错误：请输入有效的运算符！")
        except ZeroDivisionError as e:
            print(e)
        except ValueError:
            print("错误：请输入有效的整数！")
        except Exception as e:
            print(f"发生未知错误：{e}")