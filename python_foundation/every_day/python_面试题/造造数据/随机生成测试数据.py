#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 熊🐻来个🥬
# @Date:  2025/2/19
# @Description: [对文件功能等的简要描述（可自行添加）]
import faker
# 生成随机测试数据编写一个脚本，生成1000条随机用户数据
# （包括姓名、年龄、邮箱、手机号），并保存到Excel文件中。
from faker import Faker
import random
import threading
import json
from datetime import datetime, timedelta

faker = Faker()


def generate_data(num):
    data = []
    for i in range(num):
        start_time = datetime(2023, 1, 1)
        end_time = datetime.now()
        time_diff = (end_time - start_time).total_seconds()
        print(time_diff)
        random_date = start_time + timedelta(seconds=random.randrange(int(time_diff)))
        print(random_date)
        map_field = {"map_name": faker.name(), 'map_address': faker.address()}
        array_field = [faker.email(), faker.phone_number()]

        data.append({
            'id': i + 1,
            'age': random.randint(1, 100),
            'name': faker.name(),
            'money': random.uniform(10000, 8),
            'birth': random_date.strftime('%Y-%m-%d'),
            'map_field': map_field,
            'array_field': array_field,
            'customer_string': faker.text(),
            'kong': "",
            'receiv_time_house': faker.date_time().strftime('%Y-%m-%d'),
            'value': faker.password()
        })
    return data


def writer_to_json(data, file_path):
    with open(file_path, 'w+', encoding='utf-8') as f:
        for item in data:
            f.write(json.dumps(item, ensure_ascii=False) + '\n')

if __name__ == '__main__':
    num = 10
    file_path = './create_json_data.json'
    for i in range(num):
        data = generate_data(num)
        writer_to_json(data, file_path)
