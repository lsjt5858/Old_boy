#!/usr/bin/env python_study
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
