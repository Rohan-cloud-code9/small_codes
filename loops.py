#loops
vegetables = ["brinjal", "cucumber", "onion", "tomato"]
for e in vegetables:
    print(e)

tup = (1, 2, 3, 4, 5, 6)
for num in tup:
    print(num)

name = "rohan pandey"
for letters in name:
    if(letters == "d"):
        print("d found")
        break
    print(letters)
else:
    print("end")

#practice
number = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
for nums in number:
    print(nums)

number_1 = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

idx = 0

for numeral in number_1:
    if(numeral == 49):
        print("found at ", idx)
    
        break
    else:
         print("finding..")
    idx += 1

for el in range(5): #default
    print(el)

#range( start, stop, step size)
for ele in range(3, 33, 3):
    print(ele)

#practice
for num in range(1 , 101 , 1):
    print(num)
for ty in range(100, 0, -1):
    print(ty)

n = int(input("enter the number : "))
for i in range(1, 11, 1):
    print(n*i)
  
for j in range(5):
    pass
print("hey nigga")

#practice by whole
n = 5
sum = 0
k = 1
while k<= n:
    sum += k
    k += 1
print(sum)

#same q with for 
n = 8
sum = 0
for m in range(n+1):
    sum += m
print(sum)

#2nd question

n = 6
mult = 1
for l in range(1, n+1):
    mult *= l
print(mult)

#2nd question using whole
n = 5
multi = 1
z = 1
while z <= n:
    multi *= z
    z+=1
print(multi)
 

   