#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 熊🐻来个🥬
# @Date:  2024/12/25
# @Description: [对文件功能等的简要描述（可自行添加）]

# Python 数字组合，循环跳转，推导式，函数返回值与参数处理，变量作用域
'''
我们来详细讲解数字组合、循环跳转、推导式、函数参数与返回值处理以及变量作用域等 Python 编程中的重要概念。
课程模块：Python 进阶编程概念详解
目标： 深入理解 Python 编程中的高级概念，能够编写更高效、更灵活的代码。
时长： 一天
课程内容：
第一部分：数字组合
- 需求： 列出所有由 1、2、3 组成的无重复数字的三位数。
for i in range(1, 4):
    for j in range(1, 4):
        for k in range(1, 4):
            if i != j and i != k and j != k:
                print(i * 100 + j * 10 + k)
分支语句 if
分支语句用于根据条件决定程序的执行路径。
x = 5
if x > 0:
    print("x 是正数")
else:
    print("x 不是正数")
循环语句 for-in
for-in 循环用于遍历一个序列（如列表、元组、字符串等）。
for i in range(1, 6):
    print(i)  # 输出 1 到 5
循环嵌套
在循环中嵌套另一个循环，用于执行更复杂的任务。例如，打印数字组合：
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i = {i}, j = {j}")
第二部分：循环跳转
死循环：
  - 死循环是指循环条件永远为真的循环，导致程序无法正常结束。应避免编写死循环，或者在必要时使用 break 语句跳出循环。
示例（死循环，需要手动中断程序）
while True:
    print("This is an infinite loop.")
break 语句：
  - break 语句用于立即终止循环，跳出循环体。
for i in range(10):
    if i == 5:
        break  # 当 i 等于 5 时，跳出循环
    print(i) # 输出 0, 1, 2, 3, 4
continue 语句：
  - continue 语句用于跳过当前循环的剩余代码，直接进入下一次循环。
for i in range(10):
    if i % 2 == 0:
        continue  # 当 i 是偶数时，跳过本次循环
    print(i) # 输出 1, 3, 5, 7, 9
loop-else 子句：
- Python 的循环（for 和 while）可以有一个可选的 else 子句。当循环正常结束（即没有被 break 语句中断）时，else 子句中的代码会被执行。
for i in range(5):
    print(i)
else:
    print("Loop finished normally.") 循环正常结束后输出for i in range(5):if i == 3:break
    print(i)
else:
    print("Loop finished normally.") 因为break跳出，所以不执行
第三部分：推导式
推导式提供了一种简洁的方式来创建列表、元组、字典和集合。
列表推导式：
squares = [x**2 for x in range(10)]  生成 0 到 9 的平方列表
even_squares = [x**2 for x in range(10) if x % 2 == 0] 生成偶数的平方列表
print(squares)
print(even_squares)

# 基本语法: [表达式 for 变量 in 可迭代对象 if 条件]

# 示例1：创建平方数列表
squares = [x**2 for x in range(5)]
print(squares)  # 输出: [0, 1, 4, 9, 16]

# 示例2：带条件筛选偶数
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # 输出: [0, 2, 4, 6, 8]

# 示例3：多个for循环
pairs = [(x, y) for x in [1, 2] for y in ['a', 'b']]
print(pairs)  # 输出: [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]
元组推导式（生成器表达式）：
  - 元组推导式返回一个生成器对象，而不是一个元组。
squares_gen = (x**2 for x in range(10))
for i in squares_gen:
    print(i)

# 基本语法: (表达式 for 变量 in 可迭代对象)

# 示例1：创建平方数生成器
squares_gen = (x**2 for x in range(5))
print(squares_gen)  # 输出生成器对象
for num in squares_gen:
    print(num)  # 依次输出: 0, 1, 4, 9, 16
让我详细解释一下:
1. 元组推导式语法 (expression for item in iterable) 实际上创建的是一个生成器对象(generator object),而不是元组。
2. 这与列表推导式有明显区别:
列表推导式 - 直接创建列表
squares_list = [x**2 for x in range(10)]  返回列表

生成器表达式 - 创建生成器对象
squares_gen = (x**2 for x in range(10)]   返回生成器
3. 生成器的特点:
- 惰性计算(lazy evaluation) - 只在需要时才计算下一个值
- 只能迭代一次
- 内存效率高,因为不会一次性生成所有值
我们可以验证一下:
squares_gen = (x**2 for x in range(10))
print(type(squares_gen))  输出: <class 'generator'>

# 可以通过多种方式使用生成器
1. for循环
for i in squares_gen:
    print(i)

2. next()函数
squares_gen = (x**2 for x in range(10))
print(next(squares_gen))  0
print(next(squares_gen))  1
3. 转换为列表
squares_gen = (x**2 for x in range(10))
squares_list = list(squares_gen)
如果你想创建元组,应该使用 tuple() 转换:
squares_tuple = tuple(x**2 for x in range(10))
字典推导式：
square_dict = {x: x**2 for x in range(5)}
print(square_dict)

# 基本语法: {键表达式: 值表达式 for 变量 in 可迭代对象}

# 示例1：创建平方映射
squares_dict = {x: x**2 for x in range(5)}
print(squares_dict)  # 输出: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# 示例2：转换现有字典的值
prices = {'apple': 2.5, 'banana': 1.5, 'orange': 3.0}
double_prices = {k: v*2 for k, v in prices.items()}
print(double_prices)  # 输出: {'apple': 5.0, 'banana': 3.0, 'orange': 6.0}
集合推导式：
square_set = {x**2 for x in range(5)}
print(square_set)


# 基本语法: {表达式 for 变量 in 可迭代对象}

# 示例1：创建平方数集合
squares_set = {x**2 for x in range(5)}
print(squares_set)  # 输出: {0, 1, 4, 9, 16}

# 示例2：去除重复元素
numbers = [1, 1, 2, 2, 3, 3]
unique_squares = {x**2 for x in numbers}
print(unique_squares)  # 输出: {1, 4, 9}
第四部分：函数返回值与参数处理
函数返回值：
- 函数可以使用 return 语句返回一个或多个值。如果没有 return 语句，函数默认返回 None。
def add(a, b):
    return a + b

result = add(3, 5)
print(result)
参数传递：
位置参数： 按照参数的定义顺序传递参数。
def greet(name, message):
    print(f"{message}, {name}!")

greet("Alice", "Hello")  # 位置参数
关键字参数： 使用参数名来传递参数，可以不按顺序传递。
greet(message="Hi", name="Bob")  # 关键字参数
默认值参数： 在定义函数时为参数指定默认值。
def greet(name, message="Hello"):
    print(f"{message}, {name}!")

greet("Charlie")  # 使用默认值
greet("David", "Good morning")  # 覆盖默认值
可变参数：
    - *args：用于传递任意数量的位置参数，会被打包成一个元组。
def my_sum(*args):
    total = 0for num in args:
        total += num
    return total

print(my_sum(1, 2, 3))
print(my_sum(1, 2, 3, 4, 5))
    - **kwargs：用于传递任意数量的关键字参数，会被打包成一个字典。
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Eve", age=25, city="London")
混合参数：
  可以混合使用各种类型的参数，但需要遵循一定的顺序：位置参数、*args、关键字参数、**kwargs。
def my_func(a, b, *args, name="default", **kwargs):
    print(f"a: {a}, b: {b}")
    print(f"args: {args}")
    print(f"name: {name}")
    print(f"kwargs: {kwargs}")

my_func(1, 2, 3, 4, name="Alice", age=30, city="New York")



def greet(greeting, name="Guest", *args):
    print(f"{greeting}, {name}!")
    print("Other args:", args)
greet("Hello", "Alice", 25, "Engineer")
第五部分：变量作用域
- 局部变量： 在函数内部定义的变量，只能在该函数内部访问。
- 全局变量： 在函数外部定义的变量，可以在程序的任何地方访问。
- 全局变量和局部变量的优缺点：
  - 局部变量：
    - 优点：避免命名冲突，提高代码的可读性和可维护性。
    - 缺点：只能在函数内部使用，灵活性较差。
  - 全局变量：
    - 优点：可以在程序的任何地方使用，方便共享数据。
    - 缺点：容易导致命名冲突，降低代码的可读性和可维护性，容易引发意料之外的错误。
global_var = 10  # 全局变量

def my_function():
    local_var = 5  # 局部变量
    print(f"Inside function: global_var = {global_var}, local_var = {local_var}")

my_function()
print(f"Outside function: global_var = {global_var}")
# print(local_var) # 报错 NameError: name 'local_var' is not defined

def change_global():
    global global_var # 使用global关键字在函数内部修改全局变量
    global_var = 20
    print(f"Inside function: global_var = {global_var}")

change_global()
print(f"Outside function: global_var = {global_var}")

'''