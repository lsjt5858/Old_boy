#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 熊🐻来个🥬
# @Date:  2025/1/7

# Socket（套接字）是计算机网络中用于实现进程间通信（IPC）的一种机制，它可以让不同主机上的进程或同一主机上的不同进程进行数据交换。以下是对Socket的详细理解：
#
# ### 一、基本概念
# - **抽象接口**：Socket是一种抽象层，它为应用程序提供了一个统一的接口，使得应用程序无需关心底层网络的具体细节，如网络协议、数据包的封装与解析等，就能够进行网络通信。
# - **通信端点**：可以将Socket看作是网络通信中的端点，就像电话通信中的电话机一样。在网络通信中，一个Socket通常与一个特定的IP地址和端口号相关联，通过这个Socket，进程可以发送和接收数据。

# ### 二、工作原理
# 1. **创建Socket**：应用程序首先需要创建一个Socket对象，在创建Socket时，需要指定使用的网络协议（如TCP或UDP）。
#    - **TCP Socket**：提供可靠的、面向连接的通信服务。在进行数据传输之前，需要先建立连接，确保数据的可靠传输，并且按照发送的顺序接收数据。
#    - **UDP Socket**：提供无连接的、不可靠的通信服务。数据报可以随时发送，不需要事先建立连接，但不能保证数据的可靠传输和顺序。
# 2. **绑定地址和端口**：创建Socket后，通常需要将其绑定到一个本地的IP地址和端口号上（对于服务器端Socket），以便其他进程能够找到并与之通信。客户端Socket一般不需要显式绑定，系统会自动分配一个可用的端口号。
# 3. **建立连接（TCP）**：如果是TCP Socket，服务器端Socket会监听指定的端口，等待客户端的连接请求。客户端Socket则向服务器端的IP地址和端口号发起连接请求，服务器端接受请求后，连接建立成功，双方可以开始进行数据传输。
# 4. **数据传输**：连接建立后（对于TCP）或直接（对于UDP），进程可以通过Socket发送和接收数据。发送数据时，应用程序将数据写入Socket，Socket负责将数据封装成网络数据包并发送到网络上；接收数据时，Socket从网络上接收数据包，将数据提取出来并提供给应用程序。
# 5. **关闭Socket**：通信结束后，需要关闭Socket，释放相关的系统资源。
#
# ### 三、应用场景
# - **服务器-客户端架构**：如Web服务器（如Apache、Nginx）与浏览器之间的通信，邮件服务器与邮件客户端之间的通信等，通常使用TCP Socket来保证数据的可靠传输。
# - **实时通信应用**：一些对实时性要求较高但对数据可靠性要求相对较低的应用，如在线游戏、视频会议等，可能会使用UDP Socket来减少延迟。
# - **分布式系统**：在分布式系统中，不同节点之间的通信也常常通过Socket来实现，以便节点之间交换信息、协调工作等。
#
# 总之，Socket是网络编程的基础，它为应用程序提供了一种简单而有效的方式来实现网络通信，是构建各种网络应用和分布式系统的重要组件。Socket（套接字）是计算机网络中用于实现进程间通信（IPC）的一种机制，它可以让不同主机上的进程或同一主机上的不同进程进行数据交换。

# import socket
# import threading
#
#
# # 处理客户端连接的函数
# def handle_client(client_socket):
#     # 接收客户端发送的数据，最多接收1024字节
#     request = client_socket.recv(1024)
#     print(f"Received: {request.decode()}")
#     # 向客户端发送数据
#     client_socket.sendall(b'Hello, Client!')
#     # 关闭与客户端的连接
#     client_socket.close()
#
#
# # 服务器函数
# def server():
#     # 创建一个基于IPv4和TCP协议的套接字
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     # 将套接字绑定到本地地址localhost和端口12345
#     server_socket.bind(('localhost', 12345))
#     # 开始监听，允许最多5个客户端连接在队列中等待
#     server_socket.listen(5)
#     print("Server is listening on port 12345...")
#     while True:
#         # 接受客户端连接，返回客户端套接字和客户端地址
#         client_socket, addr = server_socket.accept()
#         print(f"Connection from {addr}")
#         # 为每个客户端连接创建一个新线程来处理
#         threading.Thread(target=handle_client, args=(client_socket,)).start()
#
#
# if __name__ == "__main__":
#     # 启动服务器
#     server()


# ================================================================
# ================================================================
# ================================================================
# ================================================================
# import pymysql
# from pymysql import Error
#
# class DatabaseManager:
#     def __init__(self, host, user, password, database):
#         self.connection = None
#         try:
#             self.connection = pymysql.connect(
#                 host=host,
#                 user=user,
#                 password=password,
#                 database=database,
#                 charset='utf8mb4',
#                 cursorclass=pymysql.cursors.DictCursor
#             )
#             print("数据库连接成功")
#         except Error as e:
#             print(f"连接错误: {e}")
#
#     def execute_query(self, query, params=None):
#         """执行查询操作"""
#         cursor = self.connection.cursor()
#         try:
#             cursor.execute(query, params or ())
#             if query.lower().startswith('select'):
#                 result = cursor.fetchall()
#                 return result
#             else:
#                 self.connection.commit()
#                 return cursor.rowcount
#         except Error as e:
#             print(f"执行查询错误: {e}")
#             return None
#         finally:
#             cursor.close()
#
#     def create_table(self):
#         """创建表示例"""
#         create_table_query = '''
#         CREATE TABLE IF NOT EXISTS users (
#             id INT AUTO_INCREMENT PRIMARY KEY,
#             name VARCHAR(255) NOT NULL,
#             email VARCHAR(255) UNIQUE,
#             created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#         )
#         '''
#         self.execute_query(create_table_query)
#
#     def insert_user(self, name, email):
#         """插入数据"""
#         query = "INSERT INTO users (name, email) VALUES (%s, %s)"
#         return self.execute_query(query, (name, email))
#
#     def update_user(self, user_id, new_name):
#         """更新数据"""
#         query = "UPDATE users SET name = %s WHERE id = %s"
#         return self.execute_query(query, (new_name, user_id))
#
#     def delete_user(self, user_id):
#         """删除数据"""
#         query = "DELETE FROM users WHERE id = %s"
#         return self.execute_query(query, (user_id,))
#
#     def select_all_users(self):
#         """查询所有用户"""
#         query = "SELECT * FROM users"
#         return self.execute_query(query)
#
#     def close(self):
#         """关闭数据库连接"""
#         if self.connection:
#             self.connection.close()
#
# if __name__ == "__main__":
#     db_manager = DatabaseManager("localhost", "root", "Lx123456", "liuxiong")
#     db_manager.create_table()
#
#     # ��入数据
#     user_id = db_manager.insert_user("John Doe", "john.doe@example.com")
#     print(f"Inserted user ID: {user_id}")
#
#     # 查询所有用户
#     users = db_manager.select_all_users()
#     for user in users:
#         print(user)
#
#     # 更新数据
#     db_manager.update_user(user_id, "Jane Doe")
#
#     # 查询所有用户
#     updated_users = db_manager.select_all_users()
#     for user in updated_users:
#         print(user)
#
#     # 删除数据
#     db_manager.delete_user(user_id)
#
#     # 查询所有用户

# ================================================================
# ================================================================
# ================================================================
# ================================================================

import yaml

class YAMLHandler:
    @staticmethod
    def read_yaml(file_path):
        """读取YAML文件"""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return yaml.safe_load(file)
        except Exception as e:
            print(f"读取YAML文件错误: {e}")
            return None

    @staticmethod
    def write_yaml(file_path, data):
        """写入YAML文件"""
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                yaml.dump(data, file, default_flow_style=False, allow_unicode=True)
            return True
        except Exception as e:
            print(f"写入YAML文件错误: {e}")
            return False

# YAML文件示例
example_yaml = """
# 服务器配置
server:
  host: localhost
  port: 8080
  debug: true

# 数据库配置
database:
  host: localhost
  port: 3306
  name: mydb
  users:
    - username: admin
      password: admin123
    - username: user
      password: user123

# 日志配置
logging:
  level: INFO
  file: app.log
"""

# YAML使用示例
def yaml_example():
    # 写入示例YAML
    with open('config.yaml', 'w') as f:
        f.write(example_yaml)

    # 读取YAML
    yaml_handler = YAMLHandler()
    config = yaml_handler.read_yaml('config.yaml')

    # 访问YAML数据
    if config:
        print(f"服务器端口: {config['server']['port']}")
        print(f"数据库用户: {config['database']['users'][0]['username']}")

        # 修改配置
        config['server']['port'] = 9000
        yaml_handler.write_yaml('config.yaml', config)

