#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 熊🐻来个🥬
# @Date:  2025/2/17
# @Description: [对文件功能等的简要描述（可自行添加）]
import requests
import json
import csv
from urllib import parse
from crypto.PublicKey import RSA
from crypto.Cipher import PKCS1_v1_5
import binascii
from crypto.Cipher import AES
from crypto.Util.Padding import pad
import base64
import binascii
import hashlib
import secrets

def aes_encrypt(text, key, iv):
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))
    padded_text = pad(text.encode('utf-8'), AES.block_size, style='pkcs7')
    encrypted = cipher.encrypt(padded_text)
    return base64.b64encode(encrypted).decode('utf-8')

def rsa_encrypt(text, pub_key):
    rsa_key = RSA.importKey(pub_key)
    cipher = PKCS1_v1_5.new(rsa_key)
    encrypted = cipher.encrypt(text.encode('utf-8'))
    return binascii.b2a_hex(encrypted).decode('utf-8')

def full_encrypt(text):
    # 第一次AES加密
    aes_key_1 = '0CoJUm6Qyw8W8jud'
    aes_iv = '0102030405060708'
    params = aes_encrypt(text, aes_key_1, aes_iv)

    # 第二次AES加密（使用随机密钥）
    aes_key_2 = secrets.token_hex(8)[:16]  # 生成16位随机密钥
    params = aes_encrypt(params, aes_key_2, aes_iv)

    # RSA加密随机密钥
    enc_sec_key = rsa_encrypt(aes_key_2[::-1], rsa_pub_key)  # 反转密钥

    return params, enc_sec_key

def get_comments(song_id, page=0):
    url = "https://music.163.com/weapi/comment/resource/comments/get"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Referer": "https://music.163.com/"
    }

    data = {
        "csrf_token": "",
        "cursor": str(-1 * page),  # 分页参数
        "offset": "0",
        "orderType": "1",
        "pageNo": str(page + 1),
        "pageSize": "20",
        "rid": f"R_SO_4_{song_id}",  # 歌曲ID
        "threadId": f"R_SO_4_{song_id}"
    }

    params, encSecKey = encrypted_request(json.dumps(data))
    post_data = {
        "params": params,
        "encSecKey": encSecKey
    }

    response = requests.post(url, headers=headers, data=post_data)
    return response.json()

def save_to_csv(comments, filename):
    with open(filename, 'a', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        for comment in comments:
            user = comment['user']['nickname']
            content = comment['content']
            time = comment['time']
            liked = comment['likedCount']
            writer.writerow([user, content, time, liked])

def main():
    song_id = input("请输入歌曲ID（从网页URL获取）：")
    filename = f"comments_{song_id}.csv"

    # 创建CSV文件并写入表头
    with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(['用户', '评论内容', '时间戳', '点赞数'])

    page = 0
    while True:
        print(f"正在爬取第 {page+1} 页...")
        data = get_comments(song_id, page)

        if 'data' not in data or 'comments' not in data['data']:
            print("没有更多评论了")
            break

        comments = data['data']['comments']
        save_to_csv(comments, filename)

        # 检查是否还有更多评论
        if not data['data']['hasMore']:
            print("爬取完成")
            break

        page += 1

if __name__ == "__main__":
    main()