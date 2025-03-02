#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 熊🐻来个🥬
# @Date:  2025/2/20
# @Description: 批量执行SQL查询并将结果保存为CSV文件

import pymysql
import csv
from datetime import datetime

# 数据库配置
DB_CONFIG = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "Lx123456",
    "database": "vueblog2",  # 直接指定数据库
    "charset": "utf8mb4"
}


# 生成批量插入的SQL语句（分批次提交）
def generate_insert_statements(start_id, end_id, batch_size=1000):
    """生成分批次的INSERT语句"""
    insert_statements = []
    for i in range(start_id, end_id, batch_size):
        batch_end = min(i + batch_size, end_id)
        values = []
        for j in range(i, batch_end):
            values.append(
                f"({j}, 'test_user_{j}', '测试用户_{j}', 'hashed_password', 1, "
                f"'test_{j}@example.com', 'http://example.com/avatar.png', "
                f"'{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}')"
            )
        insert_sql = (
            f"INSERT INTO user (id, username, nickname, password, enabled, email, userface, regTime) "
            f"VALUES {', '.join(values)};"
        )
        insert_statements.append(insert_sql)
    return insert_statements


# SQL语句列表（包含查询和操作语句）
SQL_QUERIES = [
    "SHOW TABLES;",
    "SELECT * FROM user LIMIT 10;",
    *generate_insert_statements(100, 200, batch_size=1000),
    "SELECT COUNT(*) FROM user;"
]


def connect_mysql():
    """连接MySQL数据库"""
    try:
        connection = pymysql.connect(**DB_CONFIG)
        print("数据库连接成功")
        return connection
    except Exception as e:
        print(f"数据库连接失败: {e}")
        return None


def execute_sql_and_save_csv(connection):
    """执行SQL并保存结果到CSV"""
    if not connection:
        return

    cursor = connection.cursor()
    try:
        for idx, query in enumerate(SQL_QUERIES):
            print(f"\n{'=' * 30} 执行第 {idx + 1} 条SQL {'=' * 30}")
            print(f"SQL: {query[:100]}...")  # 避免打印超长SQL

            # 判断是否为查询语句
            is_select = query.strip().upper().startswith("SELECT")

            if is_select:
                cursor.execute(query)
                results = cursor.fetchall()
                columns = [desc[0] for desc in cursor.description]  # 获取字段名
                file_name = f"result_{idx + 1}_{datetime.now().strftime('%Y%m%d%H%M%S')}.csv"
                save_to_csv(results, columns, file_name)
                print(f"查询结果已保存到: {file_name}")
            else:
                # 处理非查询语句（增删改）
                cursor.execute(query)
                connection.commit()
                print(f"执行成功，受影响行数: {cursor.rowcount}")

    except Exception as e:
        print(f"执行出错: {e}")
        connection.rollback()
    finally:
        cursor.close()
        connection.close()
        print("数据库连接已关闭")


def save_to_csv(data, columns, file_name):
    """保存数据到CSV文件"""
    if not data:
        print("没有数据需要保存")
        return

    try:
        with open(file_name, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(columns)  # 写入表头
            writer.writerows(data)  # 写入数据
        print(f"CSV文件保存成功: {file_name}")
    except Exception as e:
        print(f"保存CSV失败: {e}")


if __name__ == '__main__':
    conn = connect_mysql()
    if conn:
        execute_sql_and_save_csv(conn)