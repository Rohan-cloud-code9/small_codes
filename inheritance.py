#inheritance - when one class(child/derived) derives the properties of another class(parent/base).
#single inheritence
class Car():
    color = "black"
    @staticmethod
    def start():
        print("car started .. ")
    
    @staticmethod
    def stop():
        print("car stopped .. ")

class Toyota(Car):
    def __init__(self, brand):
        self.brand = brand

class Supra(Toyota): #multi level inheritance
    def __init__(self, type, brand):
        self.type = type
        super().__init__(brand) #super method is used to inherite the methods of parents class

car1 = Supra("petrol" , "gtr")
print(car1.brand)
car1.start()
car1.stop()
print(car1.color)
print(car1.type)

# multiple inheritance

class A:
    varA = "Welcome to class A"

class B:
    varB = "Welcome to class B"

class C(A, B):
    varC = "Welcome to class C"

print(C.varA)
print(C.varB)
print(C.varC)

#class method - used for changing the attributes of a class
#1st method
class Person:
    name = "anonymous"
    def changename(self, name):
        Person.name = name
p1 = Person()
p1.changename("rohan")
print(p1.name)
print(Person.name)

#2nd method
class Person:
    name = "anonymous"
    def changename(self, name):
        self.__class__.name = name

p1 = Person()
p1.changename("jitendra")
print(p1.name)
print(Person.name)

#3rd method'
class Person:
    name = "anonymous"
    @classmethod
    def changename(cls, name):
        cls.name = name

p1 = Person()
p1.changename("nigga")
print(p1.name)
print(Person.name)

#property method  - it is used so that if we change the attribute the fuction will still be working
class Student:
    def __init__(self, phy, chem, maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths
    
    @property
    def average(self):
        return str((self.phy +self.chem + self.maths)/3)

s1 = Student(34, 67, 89)
print(s1.average)
s1.phy = 78 #if we will not use property then print(s1.averge will return the old value)
print(s1.average)








