#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 熊🐻来个🥬
# @Date:  2024/12/25
# @Description: [对文件功能等的简要描述（可自行添加）]


# Python 素数，匿名函数，递归算法，阶乘，斐波那契数列
# 我们来详细讲解素数判断、匿名函数 (lambda 表达式)、排序 (sorted 函数)、递归算法，并结合阶乘和斐波那契数列等实例进行讲解。
# Python 算法与函数高级应用详解
# 目标：掌握 Python 中常见的算法思想和函数高级应用，能够编写更高效、更优雅的代码。
# 课程内容：
# 第一部分：素数
# - 定义： 素数是只能被 1 和自身整除的正整数，例如 2、3、5、7、11 等。
# - 判断素数：
import math

from python_foundation.python.week1.connect_redis import count

'''
def is_prime(num):if num <= 1:return False只需判断到平方根即可for i in range(2, int(math.sqrt(num)) + 1):if num % i == 0:return Falsereturn True测试
print(is_prime(2))   True
print(is_prime(10))  False
print(is_prime(17))  True打印100以内的所有素数for num in range(2, 101):if is_prime(num):
        print(num, end=" ")
print()
第二部分：匿名函数 (lambda 表达式)
- 定义： lambda 表达式用于创建匿名函数，即没有名称的函数。
- 语法： lambda arguments: expression
- arguments 是参数列表，expression 是一个表达式，其结果作为函数的返回值。
- 使用场景：
  - 作为高阶函数的参数，例如 map()、filter()、sorted() 等。
  - 创建简单的函数，避免定义完整的函数。
- 示例：
lambda 表达式实现加法
add = lambda x, y: x + y
print(add(3, 5))  输出 8sorted 函数使用 lambda 表达式排序
points = [(1, 3), (2, 1), (3, 2)]
points.sort(key=lambda point: point[1])  按 y 坐标排序
print(points) 输出 [(2, 1), (3, 2), (1, 3)]map 函数使用 lambda 表达式
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(squares) 输出 [1, 4, 9, 16, 25]filter 函数使用 lambda 表达式
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers) 输出 [2, 4]
- sorted() 函数实现原理：
- sorted() 函数使用 Timsort 算法，这是一种混合排序算法，结合了归并排序和插入排序的优点。它具有较好的平均性能和最坏情况下的性能。key 参数允许我们自定义排序的依据，通常使用 lambda 表达式来实现。
第三部分：递归算法
- 基本原则：
  - 基本情况（Base Case）： 递归函数必须有一个或多个基本情况，用于结束递归。
  - 递归调用（Recursive Step）： 递归函数必须调用自身，并将问题分解成更小的子问题。
递归使用举例 - 阶乘：
def factorial(n):if n == 0:  基本情况return 1else:  递归调用return n * factorial(n - 1)
print(factorial(5))  输出 120循环实现阶乘def factorial_loop(n):
    result = 1for i in range(1, n + 1):
        result *= ireturn result
print(factorial_loop(5)) 输出 120
第四部分：斐波那契数列
- 定义： 斐波那契数列是一个数列，其中每个数都是前两个数的和，例如 0、1、1、2、3、5、8、13 等。
- 递归实现：
-
def fibonacci(n):if n <= 1:  基本情况return nelse:  递归调用return fibonacci(n - 1) + fibonacci(n - 2)

输出前 10 个斐波那契数for i in range(10):
    print(fibonacci(i), end=" ")
print() 输出 0 1 1 2 3 5 8 13 21 34循环实现斐波那契数列def fibonacci_loop(n):if n <= 1:return n
    a, b = 0, 1for _ in range(2, n + 1):
        a, b = b, a + breturn b
for i in range(10):
    print(fibonacci_loop(i), end=" ")
print() 输出 0 1 1 2 3 5 8 13 21 34
递归的注意事项：
- 递归必须有基本情况，否则会导致无限递归，最终导致栈溢出。
- 递归的效率可能不如循环，因为递归调用会占用额外的栈空间。对于一些问题，循环实现可能更高效。
教学方法建议：
- 通过图示和例子来讲解递归的执行过程。
- 对比递归和循环的优缺点，以及适用场景。
- 强调 lambda 表达式的简洁性和适用性。
- 讲解 sorted() 函数的 key 参数，以及如何使用 lambda 表达式进行自定义排序。
通过以上讲解，学员应该能够掌握素数判断、匿名函数、排序、递归算法等重要的编程概念和技巧，并能够灵活运用到实际编程中。




'''
