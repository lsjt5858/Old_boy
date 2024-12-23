#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 熊🐻来个🥬
# @Date:  2024/11/28
# @Description: [对文件功能等的简要描述（可自行添加）]

# ===本地连接 Redis 数据库=======方式一 =========================================
# import redis
#
# # 创建Redis连接对象，这里连接本地Redis，默认端口是6379，db=0表示使用第一个数据库
# r = redis.StrictRedis(host='localhost', port=6379, db=0)
#
# # 可以进行一些简单的操作测试连接是否成功，比如设置一个键值对
# r.set('test_key', 'test_value')
# # 键获取刚才设置的对应的值
# result = r.get('test_key')
# print(result.decode('utf-8'))  # 因为获取的值是字节类型，需要解码为字符串类型
# # 在上述代码中：
# # 首先通过 import redis 导入 redis 模块。
# # 接着使用 redis.StrictRedis() 函数创建连接对象，参数 host 指定 Redis 服务器的主机地址，这里 'localhost' 表示本地主机；port 是 Redis 服务端口，默认是 6379；db 表示使用的数据库编号，Redis 可以有多个数据库，默认从 0 开始编号，这里选择使用第 0 个数据库。
# # 然后使用 r.set() 方法设置了一个键值对，再通过 r.get() 方法获取刚才设置的键对应的值，由于获取的值是字节类型，所以使用 decode('utf-8') 进行解码后打印输出。

# ===本地连接 Redis 数据库=== 方式二 =============================================
import redis
# 创建Redis连接对象，同样连接本地Redis，默认端口、默认数据库
r = redis.Redis()
# 进行测试操作，比如获取当前数据库中键的数量
count = r.dbsize()
print(count)

# ===本地连接 Redis 数据库 ---异常处理 =============================================
# import redis
#
# try:
#     r = redis.Redis()
#     r.ping()  # 使用ping方法测试连接是否正常，成功返回True
#     print("成功连接到Redis")
# except redis.ConnectionError as e:
#     print(f"连接Redis出现错误: {e}")