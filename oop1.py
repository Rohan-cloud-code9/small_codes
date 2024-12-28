class Student1:  # class is a blueprint to create object
    name = "karan"

s1 = Student1() #object of that student class which is building it
print(s1.name)

class Car:
    color = "blue"
    brand = "BMW"

car1 = Car()
print(car1.color)
print(car1.brand)

#constructor or nitiator fuction that always calls when we initiate object of the class
#it contains parameters but self is important amd self means the object itself (same as present object)
# we need to pass arguments in object to access the parameters in __init__() function

class Student:
    college_name = "iit bombay"
    #default constructor
    def __init__(self):
        pass
    #parameterized constructor
    def __init__(self, name, marks, rollno):
        self.name = name #things ahead of self. are object attributes
        self.marks = marks
        self.rollno = rollno
        print("adding new student in database")

student_1 = Student("karan", 56, 6)
print(student_1.name, student_1.marks, student_1.rollno)
print(student_1.college_name)

student_2 = Student("rohan", 100, 43)
print(student_2.name, student_2.marks, student_2.rollno)
print(student_2.college_name)

#object or instance attributes are the attributes which are different for each object and we need to define them like self.attr
#class attributes are those which are same for each object so we store them in class just like college_name

#2ND METHOD
class Student3:
    college_name = "abc"
    def __init__(self, name, marks, rollno):
        self.name = name
        self.marks = marks
        self.rollno = rollno
        print("here is your information student")

    def get_name(self):   #these functions are called methods
        print("your name is ", self.name)

    def get_marks(self):
        print("you scored ", self.marks)
    
    def get_rollno(self):
        print("your roll number is ", self.rollno)

student2 = Student3("rohan", 100, 43)
student2.get_name()
student2.get_marks()
student2.get_rollno()

#practice
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def hello(): # if you dont want to write self you can change this function in static method
        print("hello")
    

    def get_avg(self):
        marks = self.marks
        sum = marks[0] + marks[1] + marks[2]
        avg = sum/3
        print("hii your name is ",self.name ,"and you average score is ",avg)


student4 = Student("rohan", [100, 98, 96])
student4.get_avg()
#we can also change the names
student4.name = "akash"
student4.get_avg()
student4.hello()

#example of abstraction
class Car():
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    def start(self):
        self.clutch = True
        self.acc = True
        print("car started ..")
car1 = Car()
car1.start()

#practice
class Account():
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no

    def debit(self, amount):
        self.balance -= amount
        print(amount ,"rs was debited")
        print("total amount ",self.balance)
    
    def credit(self, amount):
        self.balance += amount
        print(amount, "rs was credited")
        print("total amount ",self.balance)

    
    def get_balance(self):
        print(self.balance)

account1 = Account(4567, 67)
account1.debit(456)
account1.credit(789)
account1.get_balance()


       
    
        



