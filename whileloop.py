i = 1
while i <= 5 :
    print("rohan")
    i += 1   #same as i = i+1

x = 1
while x <= 5:
    print(x)
    x += 1

#practice
y = 1
while y <= 100:
    print(y)
    y += 1

y = 100
while y >= 1:
    print(y)
    y -= 1

w = 3
while w <= 30:
    print(w)
    w += 3

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0
while idx <len(nums):
    print(nums[idx])
    idx += 1

#for searching an element
num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 49
idx = 0
while idx < len(num):
    if(num[idx] == x):
        print("found at index " , idx)
        break
    else :
        print("finding...")
    idx += 1

#break
t = 1
while t <= 5:
    print(t)
    if(t == 3):
        break
    t += 1

#continue used for skiping
u = 1
while u <= 5:
    if(u == 3):
        u += 1
        continue
    print(u)
    u += 1

l = 1
while l <= 10:
    if(l%2 == 0):
        l += 1
        continue
    print(l)
    l += 1






    







