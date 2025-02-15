#!/usr/bin/env python_study
# -*- coding: utf-8 -*-
# @Author: 熊🐻来个🥬
# @Date:  2025/1/7
# @Description: [对文件功能等的简要描述（可自行添加）]
import requests
from PIL import Image
from io import BytesIO

# 获取验证码
captcha_url = 'http://localhost:8081/verifyCode'
response = requests.get(captcha_url)

if response.status_code == 200:
    # 显示验证码图片
    image = Image.open(BytesIO(response.content))
    image.show()
    captcha_text = input("请输入验证码：")

    # 登录接口
    login_url = 'http://localhost:8081/doLogin'
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "content-type": "application/json;charset=UTF-8",
        "accept": "application/json, text/plain, */*"
    }
    data = {
        "username": "admin",
        "password": "123",
        "code": captcha_text
    }
    # 发送登录请求
    response = requests.post(login_url, json=data, headers=headers)

    # 检查登录是否成功
    if response.status_code == 200:
        print("登录成功")
    else:
        print("登录失败，状态码：", response.status_code)
        print("响应内容：", response.text)
else:
    print("获取验证码失败")