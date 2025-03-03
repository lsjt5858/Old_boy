#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 熊🐻来个🥬
# @Date:  2025/3/3
# @Description: [对文件功能等的简要描述（可自行添加）]


import json

class parse_all:

    def parse_har(file_path):
        """
        解析 HAR 文件，提取接口信息
        """
        # 以只读模式打开指定路径的 HAR 文件，并指定编码为 UTF-8
        with open(file_path, 'r', encoding='utf-8') as f:
            # 加载 JSON 数据到 har_data 变量
            har_data = json.load(f)

        # 初始化一个空列表，用于存储解析后的接口信息
        interfaces = []

        # 遍历 HAR 文件中 log 下的 entries 列表
        for entry in har_data.get("log", {}).get("entries", []):
            # 获取当前条目的请求信息
            request = entry.get("request", {})

            # 提取请求方法、URL、请求头、请求参数和请求体信息
            # 并将这些信息以字典形式添加到 interfaces 列表中
            interfaces.append({
                "method": request.get("method"),
                "url": request.get("url"),
                "headers": {header["name"]: header["value"] for header in request.get("headers", [])},
                "params": {param["name"]: param["value"] for param in request.get("queryString", [])},
                "body": request.get("postData", {}).get("text", None)
            })

        # 返回解析后的接口信息列表
        return interfaces






























