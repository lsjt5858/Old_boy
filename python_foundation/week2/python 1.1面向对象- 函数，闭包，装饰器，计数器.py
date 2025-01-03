#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 熊🐻来个🥬
# @Date:  2024/12/25
# @Description: [对文件功能等的简要描述（可自行添加）]
# =======================闭包 的 概念 举例  和过程 =====================================================
# def greet(name):
#     print(f"Hello, {name}!")

# 将函数赋值给变量
# greeting = greet
# greeting("Alice")  # 输出 Hello, Alice!
# ===也可以直接编写 greet("Alice")  输出同上

# 将函数作为参数传递给另一个函数
# def run_func(func, arg):
#     func(arg)

# run_func(greet, "Bob")  # 输出 Hello, Bob!

# 这个函数接受两个参数：
# func：这是一个函数对象。在Python中，函数名本身就是一个指向函数对象的引用。当你将一个函数名作为参数传递时，你实际上是在传递这个函数对象的引用。
# arg：这是一个参数，它将被传递给 func 函数。
# run_func 函数的流程
# 函数调用：当 run_func(greet, "Bob") 被调用时，greet 函数和字符串 "Bob" 被作为参数传递给 run_func。
# 参数赋值：在 run_func 函数内部，func 被赋值为 greet 函数，arg 被赋值为 "Bob"。
# 函数执行：func(arg) 这行代码实际上是在调用 func，即 greet 函数，并传递 arg，即 "Bob" 作为参数。由于 func 是 greet 的引用，这等同于直接调用 greet("Bob")。
# 输出结果：greet 函数接收到参数 "Bob" 后，执行其内部的 print 语句，输出 "Hello, Bob!"。
# 参数传递的详细说明
# 函数作为参数：在 run_func(greet, "Bob") 中，greet 是一个已经定义的函数，它被作为第一个参数传递给 run_func。这意味着 run_func 可以接收任何函数作为其第一个参数。
# 参数传递：第二个参数 "Bob" 是一个字符串，它被传递给 run_func 作为第二个参数 arg。这个参数随后被传递给 func 函数，即 greet 函数。
# 动态函数调用：run_func 函数通过 func(arg) 调用传递给它的函数对象。这种技术允许你编写更灵活的代码，因为你可以传递不同的函数给 run_func，让它执行不同的操作。
# ======================    装      饰      器   ==========================================

def decorator(func):
    def wrapper(*args, **kwargs): # *args和**kwargs用于接收任意类型的参数
        print("Before calling function.")
        result = func(*args, **kwargs)
        print("After calling function.")
        return result
    return wrapper

@decorator # 使用 @ 符号应用装饰器
def my_function():
    print("Inside function.")

my_function()
# 输出：
# Before calling function.
# Inside function.
# After calling function.



# ========================计         数       器  ========================================
def counter():
    count = 0  # 外部变量
    def increment():
        nonlocal count  # 使用外部变量 count
        count += 1
        return count
    return increment
# 创建计数器
count_func = counter()
print(count_func())  # 输出 1
print(count_func())  # 输出 2
print(count_func())  # 输出 3
print(count_func())  # 输出 4
print(count_func())  # 输出 5
