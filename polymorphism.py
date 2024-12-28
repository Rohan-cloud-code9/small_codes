#when the same operator is allowed to have different meanings according to the context
print(1 + 2) #add
print("rohan" + "pandey") #concatenate
print([1, 2, 3] + [4, 5, 6]) #merge

#adding vectors
class Vector():
    def __init__(self, x_compo, y_compo):
        self.x_compo = x_compo
        self.y_compo = y_compo
    
    def show_vector(self):
        print(self.x_compo, "i +" , self.y_compo,"j")
    
    def add(self, num2):
        new_x = self.x_compo + num2.x_compo
        new_y = self.y_compo + num2.y_compo
        return Vector(new_x, new_y)

num1 = Vector(1, 3)
num1.show_vector()
num2 = Vector(3, 6)
num2.show_vector()
num3 = num1.add(num2)
num3.show_vector()

#another way of adding vectors is dunder function
class Vector():
    def __init__(self, x_compo, y_compo):
        self.x_compo = x_compo
        self.y_compo = y_compo
    
    def show_vector(self):
        print(self.x_compo, "i +" , self.y_compo,"j")
    
    def __sub__(self, num2):
        new_x = self.x_compo - num2.x_compo
        new_y = self.y_compo - num2.y_compo
        return Vector(new_x, new_y)

num1 = Vector(1, 3)
num1.show_vector()
num2 = Vector(3, 6)
num2.show_vector()
num3 = num1 - num2 #that plus means thatb  we need to call __add__ function
num3.show_vector() #similarly for subtraction

#practice
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        r = int(self.radius)
        area = 3.14*(r)**2
        print(area)

    def get_perimeter(self):
        r = int(self.radius)
        perimeter = 2*3.14*r
        print(perimeter)

c1 = Circle(3)
c1.get_area()
c1.get_perimeter()

class Employee():
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary
     
    def showdetails(self):
        print("role =",self.role)
        print("department =" ,self.department)
        print("salary =", self.salary)

e1 = Employee("accountant", "finance", 34000)
e1.showdetails()

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("engineer", "IT", 100000)

e1 = Engineer("ROHAN" , 27)
print(e1.name)
print(e1.age)
e1.showdetails()

class Order():
    def __init__(self, item, price):
        self.item = item
        self.price = price
    
    def __gt__(self, ord2):
        return self.price > ord2.price #this is true condition
    
ord1 = Order("CHIPS", 56)
ord2 = Order("drink", 34)
print(ord1 > ord2)


    


