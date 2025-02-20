#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 熊🐻来个🥬
# @Date:  2025/2/20
# @Description: [对文件功能等的简要描述（可自行添加）]

# 批量执行SQL查询编写一个脚本，连接MySQL数据库，
# 批量执行一组SQL查询语句，并将查询结果保存到CSV文件中。

import pymysql
import csv

from python_foundation.every_day.pachong.wangyiyun import save_to_csv

SQL_QUERIES = [
    # 查询语句
    "show  databases",
    "use vueblog2",
    "show tables",
    "SELECT * FROM user;"
]

def connect_mysql():
    try:
        connect_mysql = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='Lx123456',
            charset='utf8'
        )
        print("连接数据库成功")
        return connect_mysql
    except Exception as e:
        print(f'数据库链接失败{e}')
        return None

def execute_sql_and_save_csv(connect_mysql):
    cursor = connect_mysql.cursor()
    for i,query in SQL_QUERIES:
        print(f'正在执行第{i+1}条SQL语句{query}')
        cursor.execute(query)
        records = cursor.fetchall()
        file_name = f"query_result_{i}.csv"
        save_to_csv(records, file_name)
        print(f"执行文成,受影响的行数:{cursor.rowcount}")
        cursor.close()
        connect_mysql.close()

if __name__ == '__main__':
