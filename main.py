import json
import os
import sys
from pathlib import Path

print(json.dumps({"name": "hboot", "age": 18}))
print(json.loads('{"name": "hboot", "age": 18}'))

print("------------------------------------------------------------------------------------------------------------------")

# 创建文件夹
os.mkdir("test")
# 删除文件夹
os.rmdir("test")

# 获取环境变量
print(os.environ.get("PATH"))

# 执行系统命令
os.system("ls")

print("------------------------------------------------------------------------------------------------------------------")

# 获取命令行参数
print(sys.argv)

# 获取Python解释器的版本信息
print(sys.version)

# 获取Python解释器的实现信息
print(sys.implementation)

# 获取Python解释器的平台信息
print(sys.platform)

# 获取Python解释器的路径
print(sys.executable)

print("------------------------------------------------------------------------------------------------------------------")

# 获取当前目录
print(Path.cwd())

# 获取当前目录的父目录
print(Path.cwd().parent)

# 判断路径是否存在
print(Path('.').exists())

# 拼接路径
print(Path('.') / 'test.py')

print("------------------------------------------------------------------------------------------------------------------")

import shutil

# 创建目录
# os.mkdir('test_dir')

# # 创建文件
# Path('test_dir/test.py').touch()

# # 复制文件
# shutil.copytree('test_dir', 'test_dir_copy')

# # 移动文件
# shutil.move('test_dir', 'test_dir_move')

# # 删除文件
# shutil.rmtree('test_dir_move')

import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

print("------------------------------------------------------------------------------------------------------------------")

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--name', help='your name')
args = parser.parse_args()
print(f'Hello, {args.name}')

print("------------------------------------------------------------------------------------------------------------------")

import re

# 匹配字符串
print(re.match('hello', 'hello world'))

# 提取邮箱
print(re.findall(r'[\w]+@[\w]+\.[\w]+', 'hello world, my email is <bobolity@163.com>'))

# 提取手机号
print(re.findall(r'1[3-9]\d{9}', 'hello world, my phone number is 13812345678'))

# 替换字符串
print(re.sub(r'[\d]+', '*', 'hello world, my phone number is 13812345678'))

print("------------------------------------------------------------------------------------------------------------------")

from datetime import datetime

# 获取当前时间
print(datetime.now())

# 指定时间获取对象
print(datetime(2020, 1, 1))

# 指定时间戳获取对象
print(datetime.fromtimestamp(1577836800))

# 解析字符串为时间对象
print(datetime.strptime('2020-01-01', '%Y-%m-%d'))

# 格式化时间为字符串
print(datetime.now().strftime('%Y-%m-%d'))

print("------------------------------------------------------------------------------------------------------------------")

from collections import Counter, defaultdict

print(Counter([1, 1, 2, 3, 3, 3, 4, 4, 4, 4]))
print(Counter('hello world'))

print(defaultdict(lambda: 'N/A'))
print(defaultdict(list))

print("------------------------------------------------------------------------------------------------------------------")

import random

# 生成随机数
print(random.random())

# 生成指定范围内的随机数
print(random.randint(0, 10))

# 随机选择一个元素
print(random.choice([1, 2, 3, 4, 5]))

# 随机选择指定数量的元素
print(random.sample([1, 2, 3, 4, 5], 3))

# 打乱列表
list = [1, 2, 3, 4, 5]
random.shuffle(list)
print(list)

print("------------------------------------------------------------------------------------------------------------------")

import math

# 获取圆周率
print(math.pi)

# 获取正弦值
print(math.sin(math.pi / 2))

# 获取自然对数
print(math.log(math.e))

# 获取对数
print(math.log(100, 10))

# 获取指数
print(math.exp(1))

# 获取绝对值
print(math.fabs(-100))

# 获取平方根
print(math.sqrt(16))

print("------------------------------------------------------------------------------------------------------------------")

import glob

# 获取所有文件
print(glob.glob('*.py'))

print("------------------------------------------------------------------------------------------------------------------")

import zipfile

Path('test.py').touch()
Path('test.txt').touch()

# 创建 ZIP 文件
with zipfile.ZipFile('test.zip', 'w') as zip_file:
    zip_file.write('test.py')
    zip_file.write('test.txt')

print(zipfile.is_zipfile('test.zip'))

# 读取 ZIP 文件
with zipfile.ZipFile('test.zip', 'r') as zip_file:
    print(zip_file.namelist())

print("------------------------------------------------------------------------------------------------------------------")

from itertools import product, permutations

# 笛卡尔积
for i in product([1, 2], [3, 4]):
    print(i)

# 排列组合
for i in permutations([1, 2, 3], 2):
    print(i)
