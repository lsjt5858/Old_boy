#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 熊🐻来个🥬
# @Date:  2024/12/22
# @Description: [对文件功能等的简要描述（可自行添加）]


# 打印一个简单的正方形图案
# size = 5
# for i in range(size):
#     for j in range(size):
#         print("*", end=" ")
#     print()
# # 打印一个右上角对齐的三角形
# for i in range(1, size + 1):
#     print("* " * i)


# for i  in range(1,10):
#     print('*' * i)


global_var = 10  # 全局变量


def my_function():
    local_var = 5  # 局部变量
    print(f"这是展示的全局变量{global_var},这是局部变量={local_var}")

my_function()
print(f"引用全局{global_var}")

# print(local_var) # 报错 NameError: name 'local_var' is not defined

def change_global():
    global global_var  # 使用global关键字在函数内部修改全局变量
    global_var = 20
    print(f"change 全局 = {global_var}")

change_global()
print(f"修改后全局: global_var = {global_var}")
