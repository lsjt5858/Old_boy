#!/usr/bin/env python_study
# -*- coding: utf-8 -*-
# @Author: 熊🐻来个🥬
# @Date:  2024/12/26
# @Description: [对文件功能等的简要描述（可自行添加）]

# 文件读写+错误分析+调试
'''
好的，我们来详细讲解 Python 中的文件操作，包括文件打开、文件关闭、文件读取和文件写入等。
课程模块：Python 文件操作详解
目标： 掌握 Python 中进行文件读写的基本方法，能够使用 Python 操作文件。
课程内容：
第一部分：文件打开 open()
在 Python 中，使用内置函数 open() 打开一个文件，并返回一个文件对象。
- 语法： open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
  - file：文件名（包括路径），可以是相对路径或绝对路径。
  - mode：文件打开模式，指定文件的访问权限和操作类型。
- 常用的文件打开模式：
- | 模式 | 描述 | | :--- |
- | 'r' | 只读模式（默认）。如果文件不存在，则抛出 FileNotFoundError 异常。|
- | 'w' | 写入模式。如果文件存在，则清空文件内容；如果文件不存在，则创建新文件。|
- | 'x' | 独占写入模式。如果文件已存在，则抛出 FileExistsError 异常|
- | 'a' | 追加模式。如果文件存在，则在文件末尾追加内容；如果文件不存在，则创建新文件。|
- | 'b' | 二进制模式。用于处理非文本文件（如图片、音频、视频等）。可以与其他模式组合使用，如 'rb'、'wb'。   |
- | 't' | 文本模式（默认）。用于处理文本文件。可以与其他模式组合使用，如 'rt'、'wt'。                     |
-  | '+' | 更新模式（可读可写）。可以与其他模式组合使用，如 'r+'、'w+'、'a+'。|
- 一些组合模式的含义：
  - 'r+'：读写模式。文件指针在文件开头。如果文件不存在，则抛出 FileNotFoundError 异常。
  - 'w+'：读写模式。如果文件存在，则清空文件内容；如果文件不存在，则创建新文件。
  - 'a+'：读写模式。文件指针在文件末尾。如果文件不存在，则创建新文件。
  - 'rb'、'wb'、'ab'、'rb+'、'wb+'、'ab+'：分别对应二进制模式的读、写、追加以及读写。
- 示例：
以只读模式打开文件try:
    f = open("my_file.txt", "r", encoding="utf-8") 建议指定编码方式except FileNotFoundError:
    print("File not found.")

以写入模式打开文件
f = open("new_file.txt", "w", encoding="utf-8")

以追加模式打开文件
f = open("existing_file.txt", "a", encoding="utf-8")
第二部分：文件关闭 close()
使用 close() 方法关闭文件。关闭文件可以释放系统资源，确保数据被正确写入磁盘。
- 语法： file_object.close()
- 示例：
f = open("my_file.txt", "r", encoding="utf-8")
... 对文件进行操作 ...
f.close()
- 使用 with 语句（推荐）：
- with 语句可以自动管理文件的打开和关闭，即使在发生异常时也能确保文件被正确关闭。
with open("my_file.txt", "r", encoding="utf-8") as f:... 对文件进行操作 ...文件会自动关闭
第三部分：文件读取
- read() 方法： 读取文件的全部内容。
  - 语法： file_object.read(size=-1)
    - size：可选参数，指定读取的字节数。如果省略或为负数，则读取整个文件。
  - 示例：
with open("my_file.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
- readline() 方法： 读取文件的一行内容。
  - 语法： file_object.readline()
  - 示例：
with open("my_file.txt", "r", encoding="utf-8") as f:
    line1 = f.readline()
    line2 = f.readline()
    print(line1)
    print(line2)
- readlines() 方法： 读取文件的所有行，并以列表形式返回。
  - 语法： file_object.readlines()
  - 示例：
with open("my_file.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip()) # strip() 去除每行末尾的换行符
- 迭代文件对象： 可以直接迭代文件对象，逐行读取文件内容。这是最常用的读取大文件的方式，因为它不会一次性将整个文件加载到内存中。
with open("my_file.txt", "r", encoding="utf-8") as f:for line in f:
        print(line.strip())
第四部分：文件写入
- write() 方法： 将字符串写入文件。
  - 语法： file_object.write(string)
  - 示例：
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello, world!\n")
    f.write("This is a new line.")
- writelines() 方法： 将一个字符串列表写入文件。
  - 语法： file_object.writelines(list_of_strings)
  - 示例：
lines = ["Line 1\n", "Line 2\n", "Line 3"]
with open("output.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)
- 读写文件【读取文件再次写入】
  读写文件操作结合了文件打开、读取、写入和关闭步骤。
读写文件示例：读取文件内容并将其写入到新文件
with open("example.txt", "r") as read_file:
    content = read_file.read()
with open("output.txt", "w") as write_file:
    write_file.write(content)
第五部分：其他常用文件操作方法
- seek(offset, whence): 移动文件指针的位置。offset 表示偏移量，whence 表示起始位置（0 表示文件开头，1 表示当前位置，2 表示文件末尾）。
- tell(): 返回文件指针的当前位置。
- flush(): 刷新文件内部缓冲，将缓冲区的数据立即写入磁盘。
示例：
with open("my_file.txt", "r+", encoding="utf-8") as f:
    print(f.read(5)) 读取前5个字符
    print(f.tell()) 输出当前指针位置
    f.seek(0) 将指针移动到文件开头
    f.write("New Start") 在文件开头写入内容
总结
- 文件打开：使用 open() 函数，指定文件路径和模式。
- 文件关闭：使用 close() 方法，确保文件被正确关闭。
- 文件读取：可以使用 read()、readline()、readlines() 方法读取文件内容。
- 文件写入：使用 write() 或 writelines() 方法写入文件内容。
- 读写文件：可以结合 open()、read()、write() 等方法实现文件的读取和写入操作。
- 使用 with 语句：推荐使用 with 来处理文件，它能自动管理文件的关闭，避免忘记关闭文件。


Python 中的错误分析与调试，包括错误类型、print 调试和 debug 调试。
课程模块：Python 错误分析与调试详解
目标： 掌握 Python 中常见的错误类型和调试方法，能够快速定位和解决代码中的问题。
课程内容：
第一部分：错误分析
Python 中的错误分为两种：语法错误（Syntax Errors）和异常（Exceptions）。
- 语法错误： 指代码不符合 Python 语法规则导致的错误，例如拼写错误、缺少冒号、缩进错误等。这类错误在程序运行前会被 Python 解释器检测到。
# 语法错误示例
print "Hello, world" # SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
if x > 5  # SyntaxError: invalid syntax. Perhaps you forgot a colon?
    print("x is greater than 5")
- 异常： 指程序在运行过程中遇到的错误，例如除零错误、文件未找到错误、类型错误等。这类错误会导致程序中断执行，但 Python 提供了异常处理机制来捕获和处理异常。
- 常见的异常类型：
  - NameError：访问未定义的变量。
  - TypeError：类型不匹配的操作。
  - ValueError：传入无效的参数。
  - IndexError：索引超出范围。
  - KeyError：字典中不存在的键。
  - FileNotFoundError：文件未找到。
  - ZeroDivisionError：除零错误。
  - IOError：输入/输出错误。
  - AttributeError：访问对象不存在的属性。
# 异常示例
try:
    result = 10 / 0  # ZeroDivisionError: division by zero
except ZeroDivisionError:
    print("Error: Division by zero.")

try:
    f = open("non_existent_file.txt", "r") # FileNotFoundError: [Errno 2] No such file or directory: 'non_existent_file.txt'
except FileNotFoundError:
    print("Error: File not found.")
第二部分：print 调试
print 调试是最简单也是最常用的调试方法。通过在代码的关键位置插入 print 语句，可以输出变量的值、程序的执行流程等信息，帮助我们定位问题。
- 使用 print() 函数输出变量值：
def my_function(x, y):
    print(f"x = {x}, y = {y}")  # 输出变量值
    result = x + y
    print(f"result = {result}")  # 输出计算结果
    return result

my_function(5, 10)
- 使用 print() 函数跟踪程序执行流程：
def func1():
    print("Entering func1")
    func2()
    print("Leaving func1")

def func2():
    print("Inside func2")

func1()
- print 调试的优缺点：
  - 优点：简单易用，不需要额外的工具。
  - 缺点：输出信息较多时难以管理，调试效率较低，调试完成后需要手动删除或注释 print 语句。
第三部分：debug 调试（使用 IDE 或 pdb 模块）
使用集成开发环境（IDE）的调试器或 Python 内置的 pdb 模块可以进行更高级的调试。
- 使用 IDE 调试器：
- 大多数 IDE（例如 PyCharm、VS Code 等）都提供了强大的调试器，支持断点、单步执行、变量查看等功能。
  - 设置断点： 在代码行号旁点击，设置断点。程序执行到断点处会暂停。
  - 单步执行： 使用“Step Over”（跳过）、“Step Into”（进入）、“Step Out”（跳出）等按钮控制程序的执行流程。
  - 查看变量： 在调试过程中可以查看变量的值。
  - 表达式求值： 可以在调试器中执行任意 Python 表达式。
- 使用 pdb 模块：
- pdb 是 Python 内置的调试器。可以在代码中插入 import pdb; pdb.set_trace() 语句，程序执行到此处会进入 pdb 调试模式。
import pdb

def my_function(x, y):
    pdb.set_trace()  # 进入 pdb 调试模式
    result = x + y
    return result

my_function(5, 10)
- 在 pdb 调试模式下，可以使用以下命令：
  - n (next)：执行下一行代码。
  - s (step)：进入函数调用。
  - c (continue)：继续执行程序，直到遇到下一个断点或程序结束。
  - p (print)：打印变量的值。
  - q (quit)：退出调试模式。
- debug 调试的优缺点：
  - 优点：功能强大，调试效率高，可以方便地查看变量值和控制程序执行流程。
  - 缺点：需要使用 IDE 或额外的工具，学习成本稍高。
第四部分：日志记录 (logging 模块)
logging 模块提供了比 print 更高级的日志记录功能，可以方便地管理和分析日志信息。
import logging

# 配置日志记录
logging.basicConfig(filename='my_log.txt', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def my_function(x, y):
    logging.debug(f"Entering my_function with x = {x}, y = {y}")
    try:
        result = x / y
        logging.info(f"Result: {result}")
        return result
    except ZeroDivisionError:
        logging.error("Division by zero error.")
        return None

my_function(10, 0)
my_function(10, 2)
日志级别：
- DEBUG：详细的调试信息。
- INFO：一般的信息。
- WARNING：警告信息。
- ERROR：错误信息。
- CRITICAL：严重错误信息。


'''