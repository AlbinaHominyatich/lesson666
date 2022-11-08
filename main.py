class Wow:
    def _wow(self):
        print("wow")
    def _hello(self):
        print("hello")
sofia = Wow()
sofia._hello()
sofia._wow()

class Hello:
    def __init__(self):
        print("Hello!!!")
class Hello_World(Hello):
    def __init__(self):
        super().__init__()
        print("     World")
hello_world = Hello_World()

class Computer:
    def calculate(self):
        print("Рахую...")
class Display:
    def display(self):
        print("Шось там показую")
class SmartPhone(Computer, Display):
    ...
sansung = SmartPhone()
sansung.calculate()
sansung.display()

import requests
help(requests)
def first_function():
    ...
class Site:
    ...
ITSTEP = Site
print("FOR AMIR ",requests.__cake__)

print(type("kuku"))