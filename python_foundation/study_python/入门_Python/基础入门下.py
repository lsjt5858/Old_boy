#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 熊🐻来个🥬
# @Date:  2025/3/3
# @Description: [对文件功能等的简要描述（可自行添加）]

# 十一、退出程序
'''
# 使用 exit() 来终止程序：
print("程序开始")
exit()  # 程序在此处停止，不会执行后续代码
print("这行代码不会被执行")  # 此行代码不会被执行


# 使用 sys.exit() 并传递状态码：
import sys
print("尝试正常退出...")
sys.exit(0)  # 以状态码0退出，表示正常结束


# 在函数中使用 sys.exit() 处理错误情况：
import sys
def divide(a, b):
    if b == 0:
        print("除数不能为零")
        sys.exit(1)  # 错误退出，状态码为1
    return a / b
result = divide(10, 0)


# 结合异常处理使用 sys.exit ()：
import sys
try:
    raise ValueError("触发一个值错误")
except ValueError:
    print("捕获到异常，准备退出程序")
    sys.exit(2)  # 根据异常类型选择不同的退出状态码

# 在条件语句中使用 exit ()：
user_input = input("请输入'y'来继续: ")
if user_input != 'y':
    print("用户决定退出")
    exit()  # 用户决定不继续，则退出程序
print("继续执行程序...")  # 只有当用户输入'y'时才会执行
'''
from os import getcwd

# 十二、数学运算符
'''
# 加法运算
# 减法运算
# 乘法运算
# 除法运算
# 整除和取模运算
'''


# 十三、逻辑运算符
'''
# 使用and 条件判断
# 使用or 条件判断
# 使用not 条件判断
# 组合使用逻辑运算符
# 在循环中结合逻辑运算符
for i in range(1, 11):
    if i % 2 == 0 and i % 3 == 0: 
        print(f"{i} 同时能被2和3整除") 

'''

# 十四、身份运算符
'''
# 使用 is 检查对象身份：
x = ["apple", "banana"]
y = x
print(x is y)

# 使用 is not 检查不同对象：
x = ["apple", "banana"]
z = ["apple", "banana"]
print(x is not z)


# 结合 id () 函数验证身份运算符：
x = [1, 2, 3]
y = x
print(id(x), id(y))
print(x is y)


# 在条件判断中使用身份运算符：
a = None
b = None
if a is b:
    print("a和b都是None，或者引用同一对象")

# 对比 == 和 is 的区别：
x = [1, 2, 3]
y = list(x)
print(x == y)
print(x is y)
# 解析：== 运算符比较的是两个对象的值（内容）是否相等，x 和 y 内容相同，
# 所以 x == y 为 True；is 比较的是对象的身份（是否为同一个对象） ，
# y = list(x) 创建了新列表，和 x 不是同一个对象，所以 x is y 为 False。
'''

# 十五、成员运算符
'''
# 使用 in 检查元素是否在序列中：
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("香蕉在水果列表中")

# 使用 not in 检查元素是否不在序列中：
fruits = ["apple", "banana", "cherry"]
if "orange" not in fruits:
    print("橙子不在水果列表中")

# 在循环中使用成员运算符：
for fruit in ["apple", "banana", "cherry"]:
    if fruit in ["banana", "cherry"]:
        print(f"{fruit} 是我喜欢吃的水果之一")

# 在字符串中查找字符：
sentence = "Hello, world!"
if "world" in sentence:
    print("找到了单词 'world'")


# 在字典中检查键的存在性：
student_scores = {"Alice": 90, "Bob": 85}
if "Alice" in student_scores:
    print(f"Alice的成绩是 {student_scores['Alice']}")


'''

# 十六、长度运算：len ()
'''
# 计算字符串长度：
text = "Hello, World!"
print(f"字符串 '{text}' 的长度是 {len(text)}")

# 列表元素数量统计：
numbers = [1, 2, 3, 4, 5]
print(f"列表 {numbers} 中有 {len(numbers)} 个元素")

# 元组大小：
fruits = ("apple", "banana", "cherry")
print(f"元组 {fruits} 的大小是 {len(fruits)}")

# 字典键值对数目：
person = {"name": "Alice", "age": 25, "city": "New York"}
print(f"字典中有 {len(person)} 对键值对")

# 集合元素计数：
unique_numbers = {1, 2, 2, 2, 3, 4, 4, 5}
print(f"集合 {unique_numbers} 包含 {len(unique_numbers)} 个唯一元素") 


'''

# 十七、范围生成器：range ()
'''
# 打印数字 0 到 4：
for i in range(5):
    print(i)


# 打印从 1 到 10 的偶数：
for i in range(2, 11, 2):
    print(i)
#     解析：range(2, 11, 2) 中，第一个参数 2 是起始值，第二个参数 11 是结束值（不包含 11），第三个参数 2 是步长，即每次递增 2，所以生成的序列是 2, 4, 6, 8, 10 。

# 反向打印数字 9 到 0：
for i in range(9, -1, -1):
    print(i)
# 解析：range(9, -1, -1) 中起始值是 9，结束值是 - 1（不包含 - 1），步长为 - 1，即每次递减 1，生成的序列是 9 到 0 的倒序 。

# 使用 range () 创建列表：
numbers_list = list(range(1, 6))
print(f"创建的列表是 {numbers_list}")
# 解析：range(1, 6) 生成 1 到 5 的整数序列，list() 函数将这个序列转换为列表 。

# 结合 len () 和 range () 迭代列表：
items = ["apple", "banana", "cherry"]
for i in range(len(items)):
    print(f"第{i + 1}项是{items[i]}")
# 解析：len(items) 获取列表 items 的长度，range(len(items)) 生成从 0 到列表长度减 1 的整数序列，通过索引 i 可以依次访问列表中的元素 。
'''


# 十八、切片操作
'''
# 提取列表的一部分：
my_list = [0, 1, 2, 3, 4, 5]
slice_of_list = my_list[1:4]
print(f"切片后的列表是 {slice_of_list}")
# 解析：my_list[1:4] 表示从索引 1（包含）开始，到索引 4（不包含）结束，提取列表中的元素，所以得到 [1, 2, 3]。

# 使用负索引进行切片：
my_string = "Python"
reversed_slice = my_string[-3:]
print(f"切片结果是 {reversed_slice}")

# 步长为 2 的切片：
my_tuple = (0, 1, 2, 3, 4, 5)
even_elements = my_tuple[::2]
print(f"每隔一个元素提取的结果是 {even_elements}")
# 解析：[::2] 中，第一个冒号前省略起始索引，默认从 0 开始；第二个冒号后省略结束索引，默认到序列末尾；步长为 2，即每隔一个元素提取，所以结果是 (0, 2, 4)。

# 完全反转序列：
sequence = "abcdef"
reversed_sequence = sequence[::-1]
print(f"反转后的序列是 {reversed_sequence}")

# 使用切片更新列表中的部分：
letters = ['a', 'b', 'c', 'd', 'e']
letters[1:4] = ['B', 'C', 'D']
print(f"更新后的列表是 {letters}")

'''


# 十九、列表生成式
'''
# 创建包含平方数的列表：
squares = [x**2 for x in range(1, 6)]
print(f"平方数列表是 {squares}")

# 筛选出偶数：
even_numbers = [num for num in range(1, 11) if num % 2 == 0]
print(f"偶数列表是 {even_numbers}")
# 解析：range(1, 11) 生成从 1 到 10 的整数序列，if num % 2 == 0 作为筛选条件，只有满足该条件（即能被 2 整除）的数 num 才会被添加到列表中，结果是 [2, 4, 6, 8, 10]。

# 将字符串转换为大写：
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print(f"大写单词列表是 {upper_words}")


# 生成笛卡尔积：
pairs = [(x, y) for x in [1, 2, 3] for y in ['a', 'b']]
print(f"笛卡尔积列表是 {pairs}")
# 解析：外层循环遍历 [1, 2, 3] 中的 x，内层循环遍历 ['a', 'b'] 中的 y，将每一对 (x, y) 组合添加到列表中，结果是 [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b'), (3, 'a'), (3, 'b')]。

# 根据条件过滤和转换：
mixed_data = [0, "apple", 1, "banana", 2, None, 3, ""]
filtered_data = [item for item in mixed_data if isinstance(item, int) and item > 0]
print(f"过滤并转换后的数据是 {filtered_data}")

'''


# 二十、元组定义
'''
# 定义一个简单的元组：
simple_tuple = (1, 2, 3)
print(f"简单元组是 {simple_tuple}")

# 单元素元组需要尾随逗号：
single_element_tuple = (42,)
print(f"单元素元组是 {single_element_tuple}")

# 元组解包：
coordinates = (10, 20)
x, y = coordinates
print(f"x坐标是 {x}, y坐标是 {y}")

# 不可变性示例：
immutable_tuple = (1, 2, 3)
try:
    immutable_tuple[0] = 4
except TypeError as e:
    print(f"错误信息: {e}")

# 使用元组作为字典的键：
student_scores = {(1, "Alice"): 90, (2, "Bob"): 85}
print(f"Alice的成绩是 {student_scores[(1, 'Alice')]}")

'''

# 二十一、字典定义
'''
# 创建一个简单的字典：
person = {"name": "Alice", "age": 25}
print(f"字典内容: {person}")

# 使用 dict () 构造函数创建字典：
shopping_list = {"fruits": ["apple", "banana"], "vegetables": ["carrot"]}
print(f"购物清单: {shopping_list}")

# 创建空字典并动态添加键值对：
empty_dict = {}
empty_dict["country"] = "China"
print(f"国家信息: {empty_dict}")

# 创建具有相同值的字典：
default_values = {}.fromkeys(['height', 'width'], 0)
print(f"默认尺寸: {default_values}")

'''

# 二十二、字典操作
'''
# 使用 get () 方法获取字典中的值：
user_info = {"name": "李四", "email": "lisi@example.com"}
email = user_info.get("email", "无邮箱信息")
print(f"用户邮箱: {email}")

# 使用 pop () 方法移除并返回指定键的值：
scores = {"math": 90, "english": 85}
math_score = scores.pop("math")
print(f"数学成绩已移除: {math_score}")

# 使用 update () 方法合并两个字典：
first_half = {"Q1": 100, "Q2": 200}
second_half = {"Q3": 300, "Q4": 400}
first_half.update(second_half)
print(f"全年业绩: {first_half}")

# 清空字典所有条目：
inventory = {"apples": 30, "bananas": 45}
inventory.clear()
print(f"库存清空后: {inventory}")

# 检查字典中是否存在特定键：
settings = {"theme": "dark", "language": "en"}
has_theme = "theme" in settings
print(f"是否有主题设置: {has_theme}")
'''


# 二十三、文件操作
"""
# 打开文件并读取其内容：
with open('./example.txt', 'r') as file:
    content = file.read()
    print(f"文件内容: {content}")

# 向文件写入文本：
with open('output.txt', 'w') as file:
    file.write("这是一个测试文件。")
    print("写入完成")

# 追加文本到文件末尾：
with open('output.txt', 'a+') as file:
    file.write("\n这是追加的内容。")
    print("追加完成")


# 逐行读取文件内容：
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())

# 使用 with 语句同时打开多个文件进行读写：
with open('source.txt', 'w+') as src, open('destination.txt', 'w+') as dest:
    content = src.read()
    dest.write(content)
    print("复制完成")

"""


# 二十四、异常处理
'''
# 处理文件不存在的异常：
try:
    with open('nonexistent_file.txt', 'r') as f:
        content = f.read()
except FileNotFoundError as e:
    print(f"错误: {e}")
finally:
    print("无论是否发生异常，都会执行此代码")

# 处理数值转换错误：
try:
    number = int("abc")
except ValueError as e:
    print(f"错误: {e}")

# 处理多种异常：
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"除零错误: {e}")
except Exception as e:
    print(f"其他错误: {e}")

# 使用 else 子句在没有异常时执行代码：
try:
    number = int("123")
except ValueError:
    print("输入不是一个有效的整数")
else:
    print(f"成功转换为整数: {number}")

# 在函数中使用异常处理：
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "除数不能为零"
result = divide(10, 0)
if result is not None:
    print(f"结果是: {result}")

'''

# 二十五、模块导入
# 导入整个模块：
import math
print(f"圆周率: {math.pi}")

# 从模块中导入特定功能：
from datetime import datetime
current_time = datetime.now()
print(f"当前时间: {current_time}")

# 使用别名简化模块引用：
import numpy as np
array = np.array([1, 2, 3])
print(f"数组: {array}")

# 从模块中导入所有功能（不推荐）：
from os.path import *
print(f"当前工作目录: {getcwd()}")
# 解析：from os.path import * 导入 os.path 模块中的所有功能，直接使用函数获取当前工作目录，但这种方式可能导致命名冲突，不推荐。

# 动态导入模块：
import importlib
json_module = importlib.import_module('json')
data = json_module.dumps({"key": "value"})
print(f"JSON字符串: {data}")
