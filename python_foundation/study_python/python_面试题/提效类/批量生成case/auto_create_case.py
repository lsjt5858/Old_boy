#!/usr/bin/env python_aoto_test
# -*- coding: utf-8 -*-
# @Author: 熊🐻来个🥬
# @Date:  2025/2/20
# @Description: [对文件功能等的简要描述（可自行添加）]
# 自动化生成测试用例
# 编写一个脚本，根据输入的接口参数（如{"name": "string", "age": "int"}），
# 自动生成一组边界值测试用例并输出为JSON格式。

import json

def generate_boundary_test_cases(param_schema):
    """
    根据输入的接口参数，自动生成边界值测试用例。
    :param param_schema: dict, 接口参数的定义，例如 {"name": "string", "age": "int"}
    :return: list, 生成的测试用例列表
    """
    test_cases = []
    boundary_values = {
        "string": ["", "a", "ab", "abc", "a" * 256],  # 空字符串、短字符串、长字符串
        "int": [-2147483648, -1, 0, 1, 2147483647],  # 整数边界值
        "float": [-1.0, 0.0, 1.0, 3.14, 1.7e308],  # 浮点数边界值
        "bool": [True, False],  # 布尔值
    }
    # 遍历输入的参数定义，根据每个参数的类型生成对应的测试用例
    for param_name, param_type in param_schema.items():
        # 检查参数类型是否在预定义的边界值字典中
        if param_type not in boundary_values:
            print(f"警告：参数‘{param_name}’的类型‘{param_type}’不受支持。跳过")
            continue
        # 遍历当前参数类型的边界值列表
        for value in boundary_values[param_type]:
            # 为每个边界值生成一个单独的测试用例
            test_case = {param_name: value}
            # 将生成的测试用例添加到测试用例列表中
            test_cases.append(test_case)

    return test_cases

# 示例：输入接口参数
param_schema = {
    "name": "string",
    "age": 'int'
}

# 自动生成测试用例
test_cases = generate_boundary_test_cases(param_schema)

# 使用json.dumps将测试用例列表转换为JSON格式，并设置缩进以提高可读性
output_json = json.dumps(test_cases, indent=4, ensure_ascii=False)
print(output_json)

# 将结果保存到文件
with open("generated_test_cases.json", "w", encoding="utf-8") as f:
    f.write(output_json)

print("测试用例已生成并保存到 'generated_test_cases.json'")
