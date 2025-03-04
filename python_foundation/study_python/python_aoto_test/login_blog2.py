#!/usr/bin/env python_study
# -*- coding: utf-8 -*-
# @Author: 熊🐻来个🥬
# @Date:  2025/1/18
# @Description: [对文件功能等的简要描述（可自行添加）]

import requests


def login():
    # 定义登录接口的URL
    url = "http://localhost:8084/login"
    # 准备要发送的数据
    data = {
        'username': 'sang',  # 用户名
        'password': 123  # 密码
    }
    # 发送POST请求到登录接口
    r = requests.post(url=url, data=data)

    # 打印响应的文本内容
    print(r.text)

    # 返回响应的JSON数据中的token字段
    return r.json()

result = login()
print(result)

