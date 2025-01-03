#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 熊🐻来个🥬
# @Date:  2024/12/31
# @Description: [对文件功能等的简要描述（可自行添加）]
import multiprocessing
import time

# def task(name):
#     print(f"进程 {name} 启动")
#     time.sleep(2)  # 模拟任务执行
#     print(f"进程 {name} 结束")
#
# if __name__ == "__main__":  # 必须在 if __name__ == "__main__": 中创建进程
#     p1 = multiprocessing.Process(target=task, args=("进程1",))
#     p2 = multiprocessing.Process(target=task, args=("进程2",))
#
#     p1.start() # 启动进程
#     p2.start()
#
#     p1.join()  # 等待进程 p1 结束
#     p2.join()  # 等待进程 p2 结束
#     print("所有进程结束")

import socket
import threading


# 处理客户端连接的函数
def handle_client(client_socket):
    # 接收客户端发送的数据，最多接收1024字节
    request = client_socket.recv(1024)
    print(f"Received: {request.decode()}")
    # 向客户端发送数据
    client_socket.sendall(b'Hello, Client!')
    # 关闭与客户端的连接
    client_socket.close()


# 服务器函数
def server():
    # 创建一个基于IPv4和TCP协议的套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 将套接字绑定到本地地址localhost和端口12345
    server_socket.bind(('localhost', 12345))
    # 开始监听，允许最多5个客户端连接在队列中等待
    server_socket.listen(5)
    print("Server is listening on port 12345...")
    while True:
        # 接受客户端连接，返回客户端套接字和客户端地址
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        # 为每个客户端连接创建一个新线程来处理
        threading.Thread(target=handle_client, args=(client_socket,)).start()


if __name__ == "__main__":
    # 启动服务器
    server()