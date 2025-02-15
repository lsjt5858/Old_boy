#!/usr/bin/env python_study
# -*- coding: utf-8 -*-
# @Author: 熊🐻来个🥬
# @Date:  2024/12/29
# @Description: [对文件功能等的简要描述（可自行添加）]

#
# class Animal:
#     def speak(self):
#         pass
# class Dog(Animal):
#     def speak(self):
#         print("汪汪汪!")
# class Cat(Animal):
#     def speak(self):
#         print("喵喵喵!")
# def animal_sound(animal: Animal):
#     animal.speak()
# # 创建对象
# dog = Dog()
# cat = Cat()
# animal_sound(dog)  # 输出: Woof!
# animal_sound(cat)  # 输出: Meow!




# def greet(name: str) -> None:
#     print(f"Hello, {name}!")

def greet1(name: int) -> None:
    print(f"Hello, {name}!")
    print(type(name))


greet2 = greet1
greet2("xiong")