#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 熊🐻来个🥬
# @Date:  2024/12/29
# @Description: [对文件功能等的简要描述（可自行添加）]

# 动物园
class Animal:
    total_animals = 0  # 类属性，记录动物总数

    def __init__(self, name, age):
        self.name = name        # 实例属性
        self._age = age         # 保护属性
        Animal.total_animals += 1

    def make_sound(self):       # 实例方法
        print("动物发出叫声")

    def get_age(self):
        return self._age

    @classmethod
    def get_total_animals(cls):  # 类方法
        return cls.total_animals

class Mammal(Animal):  # 继承 Animal 类
    def __init__(self, name, age, fur_color):
        super().__init__(name, age) # 调用父类的构造方法
        self.fur_color = fur_color

    def make_sound(self):  # 重写父类方法（多态）
        print("哺乳动物发出叫声")

class Dog(Mammal):
    def make_sound(self):
        print("汪汪汪")

class Cat(Mammal):
    def make_sound(self):
        print("喵喵喵")

class Bird(Animal):
    def __init__(self, name, age, feather_color):
        super().__init__(name, age)
        self.feather_color = feather_color

    def make_sound(self):
        print("鸟儿发出叫声")

# 创建动物对象
dog = Dog("旺财", 3, "棕色")
cat = Cat("咪咪", 2, "白色")
bird = Bird("鹦鹉", 5, "彩色")

# 调用方法
dog.make_sound()        # 输出：汪汪汪
cat.make_sound()        # 输出：喵喵喵
bird.make_sound()       # 输出：鸟儿发出叫声

print(f"{dog.name}的年龄是{dog.get_age()}岁") # 通过get方法访问受保护的age属性
print(f"动物园共有{Animal.get_total_animals()}只动物") # 输出：动物园共有3只动物