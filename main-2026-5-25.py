print("hello world")

name = "hboot"
age = 18
user_name = 'admin'

list = []
list.append(18)

dict = {"name": "hboot", "age": 18}
dict["name"] = "hboot"

def get_name(name,age=18):
    return f"hello, {name}! You are {age} years old."

print(get_name(dict["name"]))

get_name = lambda name, age=18: f"hello, {name}! You are {age} years old."
print(get_name(dict["name"]))


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"{self.name} is {self.age} years old.")

    def say_hello(self):
        print(f"Hello, my name is {self.name}.")
        print(f"I am {self.age} years old.")

class AdvancedPerson(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.skills = []

    def add_skill(self, skill):
        self.skills.append(skill)
        print(f"{self.name} has learned {skill}.")

person = Person("Alice", 25)
person.say_hello()

advanced_person = AdvancedPerson("Bob", 30)
advanced_person.add_skill("Python")

age = 18

if age < 18:
    print("You are a minor.")
if age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are an senior.")

list = ['apple', 'banana', 'orange']

for item in list:
    print(item)

for i in range(1, 6):
    print(i)   

i = 1
while i <= 5:
    print(i)
    i += 1

with open('log.txt','w',encoding='utf-8') as f:
    f.write('Hello World')
    f.write('\n')
    f.write('This is a test.')
    f.write('\n')

with open('log.txt','r',encoding='utf-8') as f:
    print(f.read())
    
with open('log.txt','r',encoding='utf-8') as f:
    for line in f:
        print(line)
        print(line.strip()) # 去除换行符

import math

print(math.sqrt(16))

import math as m

print(m.sqrt(16))

from math import sqrt

print(sqrt(16))

try:
    # print(1/0)
    # print(math.sqrt(-1))
    print(int('a'))

except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Invalid value.")
except:
    print("An error occurred.")
finally:
    print("Finally block executed.")

list = []
# if \ for 语句
for i in range(1, 6):
    if i % 2 == 0:
        list.append(i)

list = [x for x in range(1, 6) if x % 2 == 0]
print(list)

def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function execution.")
        result = func(*args, **kwargs)
        print("After function execution.")
        return result

    return wrapper
@decorator
def func():
    print("Function execution.")
    return "Function result."

print(func())

def get_name(*args, **kwargs):
    print(f"hello, {args[0]}! You are {kwargs['age']} years old.")

get_name("hboot", age=18)

       
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."
    def __len__(self):
        return len(self.name)


person = Person("Alice", 25)
print(person)
print(len(person))

name: str = "hboot"

def get_name(name: str) -> str:
    return f"hello, {name}!"

print(get_name([1,2,3]))

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

for i in fibonacci():
    if i > 100:
        break
    print(i)


from contextlib import contextmanager

@contextmanager
def open_file(filename,mode):
    f = open(filename,mode)
    try:
        yield f
    finally:
        f.close()

with open_file('log.txt','r') as f:
    print(f.read())  


class OpenFile:
    def __init__(self,filename,mode='r'):
        self.filename = filename
        self.mode = mode   
    def __enter__(self):
        self.f = open(self.filename,self.mode)
        return self.f
    def __exit__(self,exc_type,exc_val,exc_tb):
        if self.f:
            self.f.close()

with OpenFile('log.txt') as f:
    print(f.read())


import asyncio
import random as RANDOM
async def hello(name: str,sem: asyncio.Semaphore):
    
    async with sem:
        print(f'Hello {name}!')
        await asyncio.sleep(RANDOM.randint(1,5))
        print(f'Bye {name}!')

async def batch_hello():
    # 控制并发3
    sem = asyncio.Semaphore(3)
    
    tasks = [hello(f'name{i}',sem) for i in range(10)]
    # await asyncio.gather(*tasks)
    
    for task in asyncio.as_completed(tasks):
        await task
        
    print('All done!')
    
asyncio.run(batch_hello())
print("hello world")

