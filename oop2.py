#used to delete object properties or object itself
class Student():
    def __init__(self, name):
        self.name = name
s1 = Student("karan")
s1.name
del s1.name
print(s1.name)
del s1
print(s1)

 #private attributes are those which do not work outside class you need to add __ this to a attribute to make it private
class Account():
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass
    
    def acc(self):
        print(self.__acc_pass)

account1 = Account(1234, "abcd")
print(account1.acc_no)
print(account1.__acc_pass)

account1.acc() #it will work

#methods private
class Person():
    def __init__(self, name):
        self.name = name
    def __hello(self):
        print("welcome ",self.name)
        
p1 = Person("rakesh")
p1.__hello()


class Person():
    def __init__(self, name):
        self.name = name
    def __hello(self):
        print("welcome ",self.name)
    def welcome(self):
        self.__hello()
        
p1 = Person("rakesh")
p1.welcome()

# getters and setters 
class Voting:
    def __init__(self):
        self.__age = 0
    def set_age(self, x):
        self.__age = x
    def get_age(self):
        print(self.__age)

vote = Voting()
vote.set_age(34)
vote.get_age()









