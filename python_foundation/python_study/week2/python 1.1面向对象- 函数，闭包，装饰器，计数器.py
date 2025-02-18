#!/usr/bin/env python_study
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

# def decorator(func):
#     def wrapper(*args, **kwargs): # *args和**kwargs用于接收任意类型的参数
#         print("Before calling function.")
#         result = func(*args, **kwargs)
#         print("After calling function.")
#         return result
#     return wrapper
#
# @decorator # 使用 @ 符号应用装饰器
# def my_function():
#     print("Inside function.")

# my_function()
# 输出：
# Before calling function.
# Inside function.
# After calling function.

# ========================尝试  自己 写一个  装饰器 ========================================


import time

# 定义一个装��器，用于在函数执行前和执行后打印一些信息。以下有两个函数分别会用到
def display_time(func):
    """
    一个函数，用于在函数执行前和执行后打印一些信息。
    注意：在函数执行前和执行后，会执行此函数。
    """
    def wrapper(*args, **kwargs):
        t1 = time.time()
        print(f"函数 {func.__name__} 开始执行")
        print(f"函数 {func.__name__} 开始执行")
        result = func(*args, **kwargs)  # 执行被装��函数
        t2 = time.time()
        print(f"函数 {func.__name__} 执行结束，执行时间为 {t2 - t1:.4f} 秒")
        return result
    return wrapper


# 判断是否是质数
def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2,num):
            if num % i == 0:
                return False
        return True

@display_time
def prime_numbers(num):
    count = 0
    for i in range(2,num):
        time.sleep(1)
        if is_prime(i):
            count += 1
            print(i)
    return count
prime_numbers(5)




@display_time
def add(a,b):
    print()
    return a + b
a = int(input("请输入a"))
b = int(input("请输入a"))
res = add(a,b)
print(res)

# 以下是被装饰的函数



# ========================练习题 1  ========================================
# 题目描述：
# 编写一个装饰器 timer_decorator，用于计算被装饰函数的执行时间，并将执行时间打印出来。
# 例如，有一个函数 slow_function，它会进行一些耗时的操作（可以使用 time.sleep 模拟），
# 使用 timer_decorator 装饰后，调用 slow_function 时能输出其执行时间。
# 提示：
# 可以使用 time 模块来获取时间。

# import time
#
# # 这是原函数   可能在很多地方被调用
# def slow_function():
#     time.sleep(2)
#     print("这是原函数，用于程序耗时的操作")
#
#
# # 这是一个装饰器 在调用原函数的基础上增加额外的功能
# def timer_decorator(func):
#     def wrapper():
#         start_time = time.time()  # 获取开始时间
#         result = func()  # 执行被装饰函数
#         end_time = time.time()  # 获取结束时间
#         print(f"函数 {func.__name__} 执行时间为 {end_time - start_time:.4f} 秒")
#         return result
#     return wrapper
#
# # 通过上面的编写上面的装饰器，在来一个函数，调用装饰器-调用原函数，
# @timer_decorator
# def slow_function():
#     time.sleep(2)
#     print("这是原函数，用于程序耗时的操作")
#
# slow_function()

# ========================练习题 2  ========================================
# 题目二：
# 题目描述：
# 创建一个装饰器 retry_decorator，它可以让被装饰的函数在出现指定异常时自动重试一定次数。
# 例如，有一个函数 risky_function 可能会抛出 ValueError，使用 retry_decorator 装饰后，
# 设置重试次数为 3 次，如果 risky_function 抛出 ValueError，则自动重试，直到成功或重试次数用完。
# 提示：
# 需要使用循环和异常处理来实现重试机制。
# def retry_decorator(retry_times=3, exception_type=Exception):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(retry_times):
#                 try:
#                     return func(*args, **kwargs)
#                 except exception_type as e:
#                     print(f"捕获到异常 {e}，重试 {_ + 1} / {retry_times}")
#             print(f"重试 {retry_times} 次后仍失败")
#
#         return wrapper
#
#     return decorator


# @retry_decorator(retry_times=3, exception_type=ValueError)
# def risky_function():
#     import random
#     if random.random() < 0.5:
#         raise ValueError("模拟错误")
#     print("函数执行成功")


# risky_function()

# ========================练习题 3  ========================================
# 题目描述：
# 编写一个装饰器 log_decorator，用于记录被装饰函数的调用信息，
# 包括函数名、参数和返回值，将这些信息写入到一个日志文件中。
# 例如，有一个函数 calculate_sum，使用 log_decorator 装饰后，
# 每次调用 calculate_sum，其相关信息都会被记录到指定的日志文件中。
# 提示：可以使用 logging 模块来实现日志记录功能。
# import logging
#
#
# def log_decorator(func):
#     logging.basicConfig(filename='function_log.log', level=logging.INFO,
#                         format='%(asctime)s - %(funcName)s - %(message)s')
#
#     def wrapper(*args, **kwargs):
#         args_str = ', '.join(str(arg) for arg in args)
#         kwargs_str = ', '.join(f'{k}={v}' for k, v in kwargs.items())
#         log_msg = f'调用函数，参数为：{args_str}, {kwargs_str}'
#         logging.info(log_msg)
#         result = func(*args, **kwargs)
#         logging.info(f'函数返回值为：{result}')
#         return result
#
#     return wrapper
#
# @log_decorator
# def calculate_sum(a, b):
#     return a + b
# calculate_sum(3, 5)
#





# ==================多个 装饰器同时被调用的思路 ========================================
# import time
# def timer_decorator(func):
#     def wrapper():
#         start_time = time.time()
#         result = func()
#         end_time = time.time()
#         print(f"函数 {func.__name__} 执行时间为 {end_time - start_time:.4f} 秒")
#         return result
#     return wrapper
#
#
# def log_decorator(func):
#     def wrapper():
#         print(f"开始调用函数 {func.__name__}")
#         result = func()
#         print(f"函数 {func.__name__} 调用结束")
#         return result
#     return wrapper
#
#
# @timer_decorator
# @log_decorator
# def target_function():
#     time.sleep(1)
#     print("这是目标函数")
#
#
# target_function()

# ========================计         数       器  ========================================
# def counter():
#     count = 0  # 外部变量
#     def increment():
#         nonlocal count  # 使用外部变量 count
#         count += 1
#         return count
#     return increment
# # 创建计数器
# count_func = counter()
# print(count_func())  # 输出 1
# print(count_func())  # 输出 2
# print(count_func())  # 输出 3
# print(count_func())  # 输出 4
# print(count_func())  # 输出 5
