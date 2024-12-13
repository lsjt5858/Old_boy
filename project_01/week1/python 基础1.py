#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 熊🐻来个🥬
# @Date:  2024/12/13
# @Description: [对文件功能等的简要描述（可自行添加）]
### Python 运算符

#### 一、算术运算符
# **1. 加法（+）**
# **2. 减法（-）**
# **3. 乘法（*）**
# **4. 除法（/）**
# **5. 取余（%）**
# **6. 整除（//）**
# **7. 幂运算（**）**

# 加法
a = 10
b = 5
print(a + b)  # 输出：15

# 减法
print(a - b)  # 输出：5

# 乘法
print(a * b)  # 输出：50

# 除法 (结果总是浮点数)
print(a / b)  # 输出：2.0
print(10 / 3)  # 输出: 3.3333333333333335

# 取模（求余数）
print(a % b)  # 输出：0
print(10 % 3)  # 输出: 1
print(10 % 4)  # 输出：2

# 整除（向下取整）
print(a // b)  # 输出：2
print(10 // 3)  # 输出: 3
print(10 // 4)  # 输出：2
print(-10 // 3)  # 输出：-4。因为-3.3333向下取整是-4

# 幂运算
print(a ** b)  # 输出：100000 (10的5次方)
print(2 ** 3)  # 输出 8 (2的三次方)

#### 二、关系运算符
# **1. 等于（==）**
# **2. 不等于（!=）**
# **3. 大于（>）**
# **4. 小于（<）**
# **5. 大于等于（>=）**
# **6. 小于等于（<=）**
# **示例：**
x = 10
y = 5
z = 10

print(x == y)  # 输出：False
print(x != y)  # 输出：True
print(x > y)  # 输出：True
print(x < y)  # 输出：False
print(x >= z)  # 输出：True
print(x <= y)  # 输出：False

# 字符串比较
str1 = "hello"
str2 = "Hello"
str3 = "hello"
print(str1 == str2)  # 输出：False （区分大小写）
print(str1 == str3)  # 输出：True


#### 三、逻辑运算符
# and：与（两个操作数都为 True 时结果才为 True）
# or：或（两个操作数中至少有一个为 True 时结果就为 True）
# not：非（取反，如果操作数为 True 则结果为 False，反之亦然）
# 短路特性：
#
# and：如果第一个操作数为 False，则整个表达式的结果一定是 False，Python 不会再计算第二个操作数。
# or：如果第一个操作数为 True，则整个表达式的结果一定是 True，Python 不会再计算第二个操作数。

a = True
b = False

print(a and b)  # 输出：False
print(a or b)  # 输出：True
print(not a)  # 输出：False

# 短路特性示例
def test():
    print("test function is called")
    return True


if False and test():  # 由于第一个操作数为False，test函数不会被调用
    print("This will not be printed")

if True or test():  # 由于第一个操作数为True，test函数不会被调用
    print("this will be printed anyway")

if test() or False:  # test()函数会被调用
    print("test() call result will be used")

# 短路特性
# 当第一个条件已经决定了结果时，第二个条件不会再计算
# print(a and (1/0))  # 输出：False，不会计算 1/0，因为 a 为 True，短路


#### 四、成员运算符
# **1. `in`**
# **2. `not in`**
#
# **示例：**

# 检查元素是否在列表中
a = [1, 2, 3, 4]
print(3 in a)  # 输出：True

# 检查元素是否不在列表中
print(5 not in a)  # 输出：True

#### 五、三目运算符（条件表达式）
# **语法：** `true_expr if condition else false_expr`
# **示例：**

a = 10
b = 20

# 比较 a 和 b
result = "a is larger" if a > b else "b is larger"
print(result)  # 输出：b is larger

#### 六、身份运算符
# **1. `is`**
# **2. `is not`**
# **3. `is` 与 `==` 区别**
# **示例：**
# is 判断对象的身份是否相同
a = [1, 2, 3]
b = a
c = [1, 2, 3]

# is 判断对象是否相同（指向同一个内存地址）
print(a is b)  # 输出：True，因为 b 指向 a

print(a is c)  # 输出：False，虽然 a 和 c 的内容相同，但它们指向不同的内存地址

# == 判断对象的值是否相等
print(a == c)  # 输出：True，a 和 c 的内容相等

#### 七、总结与注意事项
# - **算术运算符** 用于基本的数学计算。
# - **关系运算符** 用于比较数值，通常用于条件判断中。
# - **逻辑运算符** 用于多条件判断，可以利用短路特性优化代码。
# - **成员运算符** 用于检查某个元素是否在容器中。
# - **三目运算符** 是简洁的条件表达式，通常用于赋值。
# - **身份运算符** 用于检查对象是否是同一个实例。
