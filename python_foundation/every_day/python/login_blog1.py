#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 熊🐻来个🥬
# @Date:  2025/1/18
# @Description: [对文件功能等的简要描述（可自行添加）]

import requests

class Login:
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def login(self):
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
        return  print(r.json())

# if __name__ == "__main__":  #
#     login_blog = Login("sang", "123")  # 创建一个 Login 实例
#     token = login_blog.login()  # 执行登录并获取 token
#     print("Token:", token)  # 打印 token
