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