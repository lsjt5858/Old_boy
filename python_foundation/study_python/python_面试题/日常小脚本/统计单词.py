#!/usr/bin/env python_aoto_test
# -*- coding: utf-8 -*-
# @Author: 熊🐻来个🥬
# @Date:  2025/2/19
# @Description: [对文件功能等的简要描述（可自行添加）]
# 1. 统计文件中单词出现次数编写一个Python脚本，读取一个文本文件，
# 统计每个单词出现的次数，并按出现次数从高到低排序输出。
import os


def word_count(file_path):
    if not os.path.exists(file_path):
        print(f"The file {file_path} does not exist.")
        return

    word_dict = {}
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            words = line.strip().split()
            for word in words:
                if word in word_dict:
                    word_dict[word] += 1
                else:
                    word_dict[word] = 1
    return word_dict


word_dict = word_count("/Users/Apple/Desktop/log/data.txt")
if __name__ == '__main__':
    file_path = "/Users/Apple/Desktop/log/data.txt"
    word_count(file_path)
    sorted_word_dict = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
    for word, count in sorted_word_dict:
        print(f"{word}: {count}")
