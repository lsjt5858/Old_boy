#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 熊🐻来个🥬
# @Date:  2025/2/19
# @Description: [对文件功能等的简要描述（可自行添加）]
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
    SECONDS = 3
    DEFAULT_KAFKA_HOST = 'kafka-cnai56df2hnanuat.kafka.ivolces.com:9093'
    DEFAULT_KAFKA_USERNAME = "xiong_zhu"
    DEFAULT_KAFKA_PASSWORD = "P@55word"

    def __init__(self, kafka_host: str = None, kafka_username: str = None, kafka_password: str = None):
        if not (kafka_host):
            self.kafka_host = kafkaProducer.DEFAULT_KAFKA_HOST
        if not (kafka_username):
            self.kafka_username = kafkaProducer.DEFAULT_KAFKA_USERNAME
        if not (kafka_password):
            self.kafka_password = kafkaProducer.DEFAULT_KAFKA_PASSWORD

        conf = {
            "bootstrap.servers": kafka_host,
            "sasl.username": username,
            "sasl.password": password,
            "sasl.mechanism": "PLAIN",
            "security.protocol": "sasl_plaintext",
        }
        self.producer = Producer(**conf)

    def produce(self, topic: str, value: Dict):
        self.producer.produce(topic=topic, value=json.dumps(value))
        self.producer.flush()


def generate_data(num):
    fake = Faker()
    data = []
    for i in range(num):
        start_date = datetime(2023, 1, 1)
        end_date = datetime.now()
        time_diff = (end_date - start_date).total_seconds()
        random_date = start_date + timedelta(seconds=random.randrange(int(time_diff)))
        map_field = {"map_name": fake.name(), "map_address": fake.address()}
        array_field = [fake.email(), fake.phone_number()]

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
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)

def write_to_kafka(topic, data):
    producer = kafkaProducer()
    producer.produce(topic, data)

if __name__ == '__main__':
    num = 10
    topic = 'test'
    file_path_prefix = '/home/bytehouse/xiong/data_'
    for i in range(num):
        data = generate_data(1000)
        file_path = file_path_prefix + str(i) + '.json'
        write_to_json(data, file_path)
        write_to_kafka(topic, data)
        time.sleep(kafkaProducer.SECONDS)