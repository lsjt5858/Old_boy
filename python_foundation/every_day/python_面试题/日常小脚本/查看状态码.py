#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 熊🐻来个🥬
# @Date:  2025/2/19
# @Description: [对文件功能等的简要描述（可自行添加）]
# 检查URL是否有效编写一个脚本，接收一个URL列表，
# 检查每个URL是否可以正常访问（返回状态码为200），并将结果保存到一个文件中。

import requests
import sys

def login_blog(username, password):
    url = "http://localhost:8084/login"
    data = {
        "username": username,
        "password": password
    }
    respnse = requests.post(url,data)
    req_url = respnse.request.url
    print(respnse.text,req_url)
    with open('./test.txt','w+')as f:
        f.write(str(req_url))


def check_url_validity(url_list, output_file):
    with open(output_file, 'w') as f:
        for url in url_list:
            try:
                response = requests.get(url, timeout=5)
                if response.status_code == 200:
                    f.write(f"{url}: OK\n")
                else:
                    f.write(f"{url}: {response.status_code}\n")
            except requests.exceptions.RequestException as e:
                f.write(f"{url}: {str(e)}\n")
                continue

    print(f"Results saved to {output_file}")


if __name__ == '__main__':
    username = 'sang'
    password = '123'
    login_blog(username, password)

