#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 熊🐻来个🥬
# @Date:  2024/12/26
# @Description: [对文件功能等的简要描述（可自行添加）]

# 打印九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{i}*{j}={i * j}", end="\t")
    print(i)
