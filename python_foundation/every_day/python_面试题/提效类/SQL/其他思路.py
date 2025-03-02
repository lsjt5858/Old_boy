#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 熊🐻来个🥬
# @Date:  2025/3/2
# @Description: [对文件功能等的简要描述（可自行添加）]

# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 熊🐻来个🥬
# @Date:  2025/2/20
# @Description: 批量执行SQL查询并将结果保存为CSV文件

import pymysql
import csv
from datetime import datetime

# 数据库配置参数
DB_CONFIG = {
    "host": "localhost",  # 数据库地址
    "port": 3306,  # 端口号
    "user": "root",  # 用户名
    "password": "Lx123456",  # 密码（注意：生产环境应使用更安全的存储方式）
    "database": "vueblog2",  # 直接指定数据库名，避免使用USE语句
    "charset": "utf8mb4"  # 使用utf8mb4支持完整Unicode字符
}


def generate_insert_statements(start_id, end_id, batch_size=1000):
    """
    生成分批次的INSERT语句

    :param start_id: 起始ID
    :param end_id: 结束ID（不包含）
    :param batch_size: 每批插入的数据量
    :return: 包含多个INSERT语句的列表
    """
    insert_statements = []
    for i in range(start_id, end_id, batch_size):
        batch_end = min(i + batch_size, end_id)
        values = []
        for j in range(i, batch_end):
            # 构造单条插入值
            values.append(
                f"({j}, 'test_user_{j}', '测试用户_{j}', 'hashed_password', 1, "
                f"'test_{j}@example.com', 'http://example.com/avatar.png', "
                f"'{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}')"
            )
        # 组合成完整的INSERT语句
        insert_sql = (
            f"INSERT INTO user (id, username, nickname, password, enabled, email, userface, regTime) "
            f"VALUES {', '.join(values)};"
        )
        insert_statements.append(insert_sql)
    return insert_statements


# SQL语句列表（包含查询和操作语句）
SQL_QUERIES = [
    "SHOW TABLES;",  # 显示数据库中的表
    "SELECT * FROM user LIMIT 10;",  # 查询前10条用户数据
    *generate_insert_statements(100, 10000, batch_size=1000),  # 生成插入语句（9900条数据分批插入）
    "SELECT COUNT(*) FROM user;"  # 统计用户总数
]


def connect_mysql():
    """连接MySQL数据库"""
    try:
        connection = pymysql.connect(**DB_CONFIG)  # 使用参数解包建立连接
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
            print(f"SQL: {query[:100]}...")  # 截断显示避免过长

            # 判断是否为查询语句
            is_select = query.strip().upper().startswith("SELECT")

            if is_select:
                cursor.execute(query)
                results = cursor.fetchall()
                # 获取字段名（从游标描述中提取）
                columns = [desc[0] for desc in cursor.description]
                # 生成带时间戳的文件名
                file_name = f"result_{idx + 1}_{datetime.now().strftime('%Y%m%d%H%M%S')}.csv"
                save_to_csv(results, columns, file_name)
                print(f"查询结果已保存到: {file_name}")
            else:
                # 执行增删改操作
                cursor.execute(query)
                connection.commit()  # 提交事务
                print(f"执行成功，受影响行数: {cursor.rowcount}")

    except Exception as e:
        print(f"执行出错: {e}")
        connection.rollback()  # 发生错误时回滚事务
    finally:
        cursor.close()
        connection.close()
        print("数据库连接已关闭")


def save_to_csv(data, columns, file_name):
    """
    保存数据到CSV文件

    :param data: 要保存的数据（二维元组）
    :param columns: 字段名列表
    :param file_name: 保存的文件名
    """
    if not data:
        print("没有数据需要保存")
        return

    try:
        with open(file_name, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(columns)  # 写入表头
            writer.writerows(data)  # 写入数据行
        print(f"CSV文件保存成功: {file_name}")
    except Exception as e:
        print(f"保存CSV失败: {e}")


if __name__ == '__main__':
    # 程序入口
    conn = connect_mysql()  # 建立数据库连接
    if conn:
        execute_sql_and_save_csv(conn)  # 执行SQL并保存结果