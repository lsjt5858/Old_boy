#!/usr/bin/env python_aoto_test
# -*- coding: utf-8 -*-
# @Author: 熊🐻来个🥬
# @Date:  2025/2/20
# @Description: [对文件功能等的简要描述（可自行添加）]

param_schema = {
    "name": "string",
    "age": 'int'
}

print(param_schema.items(),'\n',type(param_schema))
print(param_schema.keys())
print(param_schema.values())
print(param_schema.get('name'))
print(param_schema.get('name'))