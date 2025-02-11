 mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)



def myfunc():
  x = 300
  print(x)

myfunc()

def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()


x = 300

def myfunc():
  print(x)

myfunc()

print(x)

x = 300
def myfunc():
  x = 200
  print(x)
myfunc()
print(x)

def myfunc():
  global x
  x = 300

myfunc()

print(x)

def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())

def greeting(name):
  print("Hello, " + name)
import mymodule

mymodule.greeting("Jonathan")

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

import mymodule as mx

a = mx.person1["age"]
print(a)

import platform

x = platform.system()
print(x)

def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

import datetime

x = datetime.datetime.now()
print(x)

import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))


import datetime

x = datetime.datetime(2020, 5, 17)

print(x)


import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))


x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

x = abs(-7.25)

print(x)

import math

x = math.sqrt(64)

print(x)


import math

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1
import json

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))