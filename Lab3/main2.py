class str:
    def __init__(self):
        self.text = ""

    def get(self):
        self.text = input("Write a text: ")

    def out(self):
        print(self.text)


string = str()

string.get()

string.out()

class Shape:

    def __init__(self):

        pass

    def area(self):

        return 0

class Square(Shape):

    def __init__(self, length):

        self.length = length

    def area(self):

        return self.length ** 2

shape = Shape()

print("Shape area is:", shape.area())

a = int(input("Write a length of square: "))

square = Square(a)

print("Square area is:", square.area())

class Shape:

    def __init__(self):

        pass

    def area(self):

        return 0

class Rectangle(Shape):

    def __init__(self, length, width):

        self.length = length

        self.width = width

    def area(self):

        return self.length * self.width

a = int(input("Write a length of rectangle: "))

b = int(input("Write a width of rectangle: "))

rectangle = Rectangle(a, b)

print("Rectangle area is:", rectangle.area())

import math


class Point:

    def __init__(self, x, y):
        self.x = x

        self.y = y

    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x

        self.y = new_y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)


a_1 = int(input("Write x: "))

b_1 = int(input("Write y: "))

p1 = Point(a_1, b_1)

c = int(input("Write another x: "))

d = int(input("Write another y: "))

p2 = Point(c, d)

p1.show()
p2.show()

a_2 = int(input("Write new x: "))

b_2 = int(input("Write new y: "))

p1.move(a_2, b_2)
p1.show()

print("Distance between points:", p1.dist(p2))


class Account:

    def __init__(self, owner, balance=0):
        self.owner = owner

        self.balance = balance

    def dep(self, cnt):
        self.balance += cnt

        return f"Deposit successful! New balance: {self.balance}"

    def wit(self, num):
        if num > self.balance:
            return "Withdrawals may not exceed the available balance."

        self.balance -= num

        return f"Withdrawal successful! New balance: {self.balance}"

    def show_balance(self):
        return f"Account balance: {self.balance}"


name = str(input("Write your name: "))

balance = int(input("Write your started balance: "))

acc = Account(name, balance)

print(acc.show_balance())

depos = int(input("Write a value of deposite: "))

print(acc.dep(depos))

minus = int(input("Write a withdraw: "))

print(acc.wit(minus))

another_minus = int(input("Write an another withdraw: "))

print(acc.wit(another_minus))

a = int(input("Write a number of elements: "))

lst = []

for i in range(a):

    num = int(input("Write an element of list: "))

    lst.append(num)

prime_numbers = list(filter(lambda num: all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)) and num > 1, lst))

print("Prime numbers:", prime_numbers)


x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))


def myfunc(n):
  return lambda a : a * n

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))


class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)

class Person:
  def __init__(self, name, age):
      self.name = name
      self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()


class Student(Person):
    pass


class Student(Person):
  def __init__(self, fname, lname):
    #add properties etc.

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)


class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear) 