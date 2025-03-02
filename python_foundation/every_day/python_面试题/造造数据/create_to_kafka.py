#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 熊🐻来个🥬
# @Date:  2025/2/19
# @Description: [该脚本用于生成模拟数据，并将其写入JSON文件和Kafka主题中。
# 通过Faker库生成随机数据，使用Confluent Kafka库将数据发送到Kafka。]
import os
import sys
import json
import random
import time
import threading
from datetime import datetime, timedelta
from typing import Dict
from faker import Faker
from confluent_kafka import Producer


class kafkaProducer:
    # 类常量定义
    SECONDS = 3 # 每次写入Kafka的时间间隔（秒）
    DEFAULT_KAFKA_HOST = 'kafka-cnai56df2hnanuat.kafka.ivolces.com:9093'     # 默认Kafka主机地址
    DEFAULT_KAFKA_USERNAME = "xiong_zhu"    # 默认Kafka用户名
    DEFAULT_KAFKA_PASSWORD = "P@55word"      # 默认Kafka密码

    def __init__(self, kafka_host: str = None, kafka_username: str = None, kafka_password: str = None):
        if not (kafka_host):
            self.kafka_host = kafkaProducer.DEFAULT_KAFKA_HOST
        if not (kafka_username):
            self.kafka_username = kafkaProducer.DEFAULT_KAFKA_USERNAME
        if not (kafka_password):
            self.kafka_password = kafkaProducer.DEFAULT_KAFKA_PASSWORD

        # 配置Kafka生产者的连接参数
        conf = {
            "bootstrap.servers": self.kafka_host,
            "sasl.username": self.kafka_username,
            "sasl.password": self.kafka_password,
            "sasl.mechanism": "PLAIN",      # SASL认证机制
            "security.protocol": "sasl_plaintext",      # 安全协议
        }
        # 创建Kafka生产者实例
        self.producer = Producer(**conf)

    def produce(self, topic: str, value: Dict):
        """
        向指定的Kafka主题发送消息。
        :param topic: Kafka主题名称。
        :param value: 要发送的消息内容（字典格式）。
        """
        # 将字典转换为JSON字符串并发送到Kafka
        self.producer.produce(topic=topic, value=json.dumps(value))
        # 确保消息被立即发送
        self.producer.flush()


def generate_data(num):
    """
    生成指定数量的随机数据。
    :param num: 要生成的数据条数。
    :return: 包含随机数据的列表。
    """
    # 初始化Faker实例，用于生成随机数据
    fake = Faker()
    data = []
    for i in range(num):
        # 生成随机日期
        start_date = datetime(2023, 1, 1)
        end_date = datetime.now()
        time_diff = (end_date - start_date).total_seconds()
        random_date = start_date + timedelta(seconds=random.randrange(int(time_diff)))
        # 构造嵌套字段
        map_field = {"map_name": fake.name(), "map_address": fake.address()}
        array_field = [fake.email(), fake.phone_number()]

        # 构造单条数据
        data.append({
            'id': i + 1,
            'age': random.randint(1, 100),
            'name': fake.name(),
            'money': random.uniform(10000, 8),
            'birth': random_date.strftime('%Y-%m-%d'),
            'map_field': map_field,
            'array_field': array_field,
            'customer_string': fake.text(),
            'kong': "",
            'receiv_time_house': fake.date_time().strftime('%Y-%m-%d'),
            'value': fake.password()
        })
    return data


def write_to_json(data, file_path):
    """
    将数据写入JSON文件。
    :param data: 要写入的数据（列表或字典）。
    :param file_path: JSON文件路径。
    """
    with open(file_path, 'w', encoding='utf-8') as f:
        # 写入JSON文件，确保中文字符不被转义
        json.dump(data, f, ensure_ascii=False)

def write_to_kafka(topic, data):
    """
    将数据写入Kafka主题。
    :param topic: Kafka主题名称。
    :param data: 要写入的数据（列表或字典）。
    """
    # 初始化Kafka生产者
    producer = kafkaProducer()
    # 发送数据到Kafka
    producer.produce(topic, data)

if __name__ == '__main__':
    # 主程序入口
    num = 10        # 要生成的JSON文件数量
    topic = 'test'      # Kafka主题名称
    file_path_prefix = '/home/bytehouse/xiong/data_'     # JSON文件路径前缀
    for i in range(num):
        data = generate_data(1000)
        # 构造JSON文件路径
        file_path = file_path_prefix + str(i) + '.json'
        #
        write_to_json(data, file_path)
        # 将数据写入Kafka
        write_to_kafka(topic, data)
        # 每次写入后暂停3秒
        time.sleep(kafkaProducer.SECONDS)