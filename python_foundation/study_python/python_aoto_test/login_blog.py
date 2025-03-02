#!/usr/bin/env python_study
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
        url = "http://localhost:8084/login"
        
        data = {
            'username': self.username,
            'password': self.password
        }

        r = requests.post(url=url, data=data)
        print(r.text)
        return r.json()["token"]
    def get_userinfo(self, token):
        url = "http://localhost:8084/getUserInfo"
        headers = {"Authorization": f"Bearer {token}"}
        r = requests.get(url=url, headers=headers)
        print(r.text)
        return r.json()
    def logout(self, token):
        url = "http://localhost:8084/logout"
        headers = {"Authorization": f"Bearer {token}"}
        r = requests.get(url=url, headers=headers)
        print(r.text)
        return r.json()
    def refresh_token(self, token):
        # 定义刷新令牌的URL
        url = "http://localhost:8084/refreshToken"
        # 定义请求头，包含授权信息
        headers = {"Authorization": f"Bearer {token}"}
        # 发送GET请求，获取新的令牌
        r = requests.get(url=url, headers=headers)
        # 打印响应文本
        print(r.text)
        # 返回响应中的新令牌
        return r.json()["token"]
    def delete_user(self, token):
        url = "http://localhost:8084/deleteUser"
        headers = {"Authorization": f"Bearer {token}"}
        r = requests.get(url=url, headers=headers)
        print(r.text)
        return r.json()
    def update_user(self, token):
        url = "http://localhost:8084/updateUser"
        headers = {"Authorization": f"Bearer {token}"}
        r = requests.get(url=url, headers=headers)
        print(r.text)
        return r.json()
    