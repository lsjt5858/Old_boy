#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 熊🐻来个🥬
# @Date:  2025/3/2
# @Description: [对文件功能等的简要描述（可自行添加）]
# 一、打印输出：print()输出字符串：
# ============================ ============================ ============================
# 输出简单的欢迎信息
'''
print("欢迎来到Python编程世界！")

# 输出变量值：
age = 20
name ="Alice"# 输出变量的值，使用逗号分隔不同的参数
print("你好,", name)
print(f"你好,{name}")
print("你好,%s" %name)
print("你好, {}".format(name))
print("你好, {n}，你的年龄是{a}岁。".format(n=name, a=age))
name = "Alice"
age = 20
print("你好, {0}，你的年龄是{1}岁。再次问候，{0}。".format(name, age))

# 控制输出不换行：
# 使用end参数控制输出后不换行，默认是换行符'\n'
print("这是第一行", end=" ")
print("这是第一行", end="\n")
print("这是在同一行继续输出的内容")
'''

# 二、变量定义与赋值
'''
# ============================ ============================ ============================
# 同时为多个变量赋值：
x, y, z = 1, 2, 3
print(x, y, z)  # 输出所有变量的值

# 重新赋值变量：
# 变量可以被重新赋值
counter = 0
counter = counter + 1
print(counter) # 输出更新后的值
'''

# 三、数据类型转换
'''
# ============================ ============================ ============================
# 字符串转整数：
# 将字符串形式的数字转换为整数
num_str = "100"
num_int = int(num_str)
print(num_int)  # 输出转换后的整数

# 浮点数转字符串：
# 将浮点数转换为字符串
num_float = 3.14
num_str = str(num_float)
print(num_str, type(num_str))  # 输出转换后的字符串

# 列表转元组：
# 将列表转换为元组
list_items = [1, 2, 3]
tuple_items = tuple(list_items)
print(tuple_items)  # 输出转换后的元组

# 元组转集合：
# 将元组转换为集合，去除重复元素
tuple_data = (1, 2, 2, 3, 4, 4)
set_data = set(tuple_data)
set_data1 = list(tuple_data)
print(set_data, type(set_data))  # 输出转换后的集合
print(set_data1, type(set_data1))  # 输出转换后的列表

# 创建字典：
# 使用键值对创建字典
dict_data = dict(name="李四", age=30)
print(dict_data,"以上的内容是",type(dict_data),"类型")  # 输出字典
'''

# 四、条件语句
'''
# ============================ ============================ ============================
# 简单的if条件判断：
# if...else结构：
# if...elif...else结构：
user_input = 3
if user_input == 1:
    print("选择了选项一")
elif user_input == 2:
    print("选择了选项二")
else:
    print("选择了其他选项")
'''

# 五、循环语句
'''
# ============================ ============================ ============================
# for循环遍历列表：
fruits = ["苹果","香蕉","橙子"]
for fruit in fruits:
    print(fruit) # 遍历列表中的每个元素，并打印出来

# for循环结合range函数：
for i in range(1,5): # 从1开始到4结束（不包括5）
    print(i)   # 打印当前索引

# while循环：
count = 0
while count < 5:
    print(count) # 当count小于5时，打印count的值
    count += 1 # 每次循环后增加count的值

# for循环与列表解析：
squares = [x**2 for x in range(10)]
for square in squares:
    print("后边的数字",square)  # 使用列表解析生成平方数列表，并遍历打印

# 带有break语句的循环：
for number in range(1,10):
    if number == 5:
        break
    print(number)


'''
# 六、函数定义
'''
# ============================ ============================ ============================
# 定义一个简单的函数：
def greet():
    """这是一个简单的问候函数"""
    print("你好, 欢迎来到Python的世界!")  # 打印欢迎信息
greet()  # 调用greet函数


# 带参数的函数定义：
def say_hello(name):
    """根据传入的名字打印个性化问候"""
    print(f"你好, {name}!")  # 使用f-string格式化字符串
say_hello("小明")  # 调用say_hello函数并传递参数


# 返回值的函数：
def fan_hiu_zhi_function(name,dongwu = "狗"):
    """描述宠物信息"""
    print(f"我有一只{dongwu}叫{name}")
fan_hiu_zhi_function('来福')
fan_hiu_zhi_function("旺财",dongwu="猫")    # 传递所有参数调用fan_hiu_zhi_function函数


# 可变数量参数的函数：
def ke_bian_function(*food):
    """打印顾客点的所有食物"""
    print("\n制作过油肉需要以下食物")
    for i in food:
        print(f" - {i}")
ke_bian_function('肉','青椒','🫑','🐷','大豆油','葱')     # 调用ke_bian_function函数并传递多个参数


'''


# 七、调用函数
'''
# ============================ ============================ ============================
# 调用无参函数：
def welcome_message():
    """显示欢迎消息"""
    print("欢迎使用我们的服务!")
welcome_message()  # 直接调用函数


# 调用带参数的函数：
def display_message(message):
    """显示传递的消息"""
    print(message)
display_message("这是通过函数传递的消息。")  # 调用函数并传递参数


# 调用返回值的函数：
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')  # 调用函数获取返回值
print(musician)  # 打印返回值


# 调用带有关键字参数的函数：
def keywords_function(first, last, **user_info):
    """创建一个字典,其中包含我们知道的有关用户的一切"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = keywords_function('xiong', 'ge', location='hangzhou')
print(user_profile)  # 调用函数并传递关键字参数


# 调用可变参数的函数：
def ke_bian_function(*items):
    """制作蛋糕"""
    print('\n 正在为你制作蛋糕🍰')
    for item in items:
        print(f" - {item}")
ke_bian_function('火腿', '奶酪', '生菜')
print(ke_bian_function,type(ke_bian_function))           # 调用函数并传递多个参数
'''


# 八、输入函数
"""
# ============================ ============================ ============================
# 获取用户输入并输出：
name = input("请输入您的名字: ")  # 提示用户输入
print(f"您好, {name}!")  # 输出用户输入的名字


# 获取数字输入并进行计算：
age = int(input("请输入您的年龄: "))  # 将输入转换为整数
next_year_age = age + 1
print(f"明年您将会是 {next_year_age} 岁。")


# 获取多个输入并存储在列表中：
list1 = []           # 创建空列表来保存爱好
list2 = input("请输入你的兴趣,如要结束请输入 '结束' 停止:  \n")
while list2 != '结束':
    list1.append(list2)      # 添加到列表
    list2 = input("请输入您下一个兴趣:  ")
print("您的兴趣有:", list1)


# 处理浮点数输入：
height = float(input("请输入您的身高 (米) : "))
weight = float(input("请输入您的体重 (千克) : "))
bmi = weight / (height * height)  # 计算BMI指数
print(f"您的BMI指数是 {bmi:.2f}")  # 格式化输出保留两位小数


# 结合条件判断处理输入：
answer = input("您喜欢编程吗? (yes/no): ")
if answer.lower() == 'yes':
    print("太棒了, 继续加油!")
else:
    print("没关系, 每个人都有自己的兴趣。")


# 结合条件判断处理输入：
answer = input("您喜欢编程吗? (yes/no): ")
if answer.lower() == 'yes':
    print("太棒了, 继续加油!")
else:
    print("没关系, 每个人都有自己的兴趣。")

"""


# 九、注释
'''
# ============================ ============================ ============================
# 单行注释示例：
# 这是一个单行注释
print("Hello, World!")  # 在打印语句后添加注释

# 多行注释示例：
"""
这是一段多行注释,
用来解释下面这段代码的功能。
"""
print("这是一段测试代码。")


# 文档字符串示例：
def square_number(n):
    """
    返回给定数字的平方。
    参数 n: 要求平方的数字
    返回: 数字的平方
    """
    return n * n
print(square_number(4))  # 调用square_number函数

# 使用注释来临时禁用代码：
# print("这条消息不会被打印出来。")
print("这条消息会被打印出来。")


# 注释用于调试和说明复杂逻辑：
# 计算阶乘
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)  # 递归调用自身
print(factorial(5))  # 输出5的阶乘
'''




# 十、缩进
# ============================ ============================ ============================
# 正确缩进的 if 语句：
age = 20
if age >= 18:
    print("成年人")  # 正确缩进，属于if块
print("检查完成")  # 不属于if块

# 循环中的正确缩进：
for i in range(5):
    print(i)  # 每次循环都会执行，并且正确缩进
print("循环结束")  # 循环结束后执行，不缩进

# 函数体内的正确缩进：
def my_function():
    print("这是函数内部的代码")  # 函数体内的代码必须缩进
my_function()  # 调用函数

# 错误的缩进会导致语法错误：
def another_function():
    print("如果没有正确缩进，会抛出IndentationError")  # 修正后的代码，原代码少缩进会报错

# 嵌套结构中的缩进：
if True:
    print("外层条件成立")
    if False:
        print("内层条件不成立")  # 内层条件的代码块
    else:
        print("内层条件成立")  # 内层else部分的代码块

