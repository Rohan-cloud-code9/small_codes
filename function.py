#Function definition 
def cal_sum(a, b): #a and b are parameters of function
    sum = a+b
    return sum
    
   
print(cal_sum(1, 2)) #function call and (1, 2) are called as arguments

#2nd method
def cal_mult(a, b):
    mult = a*b
    print(mult) # but i prefer to use the return thing

cal_mult(4, 2)

def print_hello(): #without parameter
    print("hello")

print_hello()

# average of three no
def cal_avg(a, b, c):
    avg = (a+b+c)/3
    print(avg)
    return avg
 
cal_avg(1, 2, 3)

print("rohan", end = " ")  #end is automatically "/n"
print("pandey")

#practice
#1
def len_func(a):
    length = len(a)
    print(length)
    return length

len_func([1, 2, 3, 4, 5, 6, 7, 8, 9])

#2nd method
cities = ["jalalpur", "farrukhabad", "firozabad", "kanpur"]
names = ["thor", "rohan", "rohit", "rahul", "rishu", "vipin", "pandey", "suresh"]
def calc_len(list):
    print(len(list))
    
calc_len(cities)
calc_len(names)
len_func(cities)

#2
def print_elem(list):
    for item in list:
        print(item, end = " ")
        
    
print_elem(cities)
print(".")

#3
def calc_fact(n):
    prod = 1
    for i in range(1, n+1):
        prod *= i
    print(prod)

calc_fact(5)
calc_fact(9)

#4
def usd_to_inr(a):
    conv = 83*a
    return conv
usd = int(input("enter the currency in usd : "))
print(usd, "dollors is", usd_to_inr(usd), "rupees in inr")



#5
def type_func(a):
    if(int(a)%2 == 0):
        print("even")
    else:
        print("odd")
    
type_func(78)
type_func(7)

#RECURSION
#print numbers from n to 1
def  show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)
    print("end")

show(5)

def fact(n): #pure example of call stack
    if(n == 0 or n == 1):
        return 1
    return n*fact(n-1)

print(fact(5))

#practice
def sum(n):
    if(n == 0):
        return 0
    return n + sum(n-1)

print(sum(6))

def elem(list, index):
    if(index == len(list)):
        return
    print(list[index])
    elem(list, index + 1)

names = ["rohan", "rahul", "rakesh", "vipin", "gokul"]
elem(names, 0 )
    


  
