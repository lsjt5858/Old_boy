#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 熊🐻来个🥬
# @Date:  2025/1/5
# @Description: [对文件功能等的简要描述（可自行添加）]

# Pytest 命名规则
# Pytest 有一套命名规则，用于识别测试文件、测试类和测试函数。
# 模块命名
# - 文件名命名：Pytest 会自动识别以 test_ 开头的文件作为测试文件。例如：
#   - test_example.py
#   - test_calculator.py
# - 不推荐：文件名中包含下划线 _ 之外的符号（如 #, . 等），以确保文件在所有操作系统上都能兼容。
# 类命名
# - 类名命名：类名应以 Test 开头（注意大小写），例如：
#   - class TestAddition:
#   - class TestCalculator:
# - 不推荐：使用小写或其他非标准命名（例如 class AddTest）。
# 方法命名
# - 方法名命名：方法名应以 test_ 开头，这样 Pytest 才能识别为测试方法。例如：
#   - def test_addition():
#   - def test_subtraction():
# - 不推荐：方法名不以 test_ 开头。

import random

# def test_addition():
#     a = random.randint(1, 10)
#     b = random.randint(1, 10)
#     result = a + b
#     print(result)
#     assert result == a + b
#
# def test_subtraction():
#     assert 5 - 3 == 2
# ============================================================================
import pytest


class TestDatabase:
    def setup_method(self):  # 每个测试方法前执行
        print("连接数据库")
        self.conn = "database connect"

    def teardown_method(self):  # 每个测试方法后执行
        print("关闭数据库连接")
        self.conn = None

    def test_insert_data(self):
        print("测试插入数据")
        assert self.conn is not None

    def test_query_data(self):
        print("测试查询数据")
        assert self.conn is not None


def test_string_contains():
    s = "hello"
    assert "he" in s
    assert "world" not in s


def test_list_contains():
    l = [1, 2, 3]
    assert 3 in l
    assert 5 not in l
    assert 4 not in l


def test_boolean_value():
    x = 1
    assert bool(x)  # x 不为 0，布尔值为 True
    y = 0
    assert not bool(y)  # y 为 0，布尔值为 False
