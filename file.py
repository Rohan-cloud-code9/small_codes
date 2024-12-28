#reading a file
f = open("sui.txt", "r")
#if you already read it then you cant readline by line

line_1 = f.readline()
print(line_1)
line_2 = f.readline()
print(line_2)
# it will proceed from the remaining data which is left for the reading
data =f.read()
print(data)
f.close()

#writing a file
#1st method
f = open("write.txt", "w")
data = f.write("i am jett main") # this overites the file
f.close()
#2nd method
f = open("write.txt", "a")
f.write("\nreyna is also my main") #this add the data in file
f.close()

#you can also make a file with either "w" or "a"
f = open("magicfile.txt", "a")
f.close()

f = open("magicfile.txt", "r+") #nothing will be erased and pointer is at the start
f.write("nigga")
f.close()

f = open("magicfile.txt", "w+") #everything wil erase
f.write("rohan is a boy")
f.close()

f = open("magicfile.txt", "a+") #pointer is at the end
f.write("\nnigga is a boy")

#another method to open the file and it automatically close the file
with open("write.txt", "r") as f:
    print(f.read())

#deleting a file
import os 
os.remove("file1.txt")

#practice
f = open("practice.txt", "w")
f.write("hii everyone\nwe are learning file I/O\nusing java\ni like programming in java")
f.close()

f = open("practice.txt", "r")
data = f.read()
new_data = data.replace("java", "python")
f.close()

f = open("practice.txt", "w")
f.write(new_data)
f.close()


def searching():
    f = open("practice.txt", "r")
    word = "learning"
    data = f.read()
    if(data.find(word) != -1):
        print("found")
    else:
        print("not found")
    f.close()
    
searching()

def check_for_line():
    word = "learning"
    f = open("practice.txt", "r")
    data = True # this means jab tak data me koi value hai
    line_no = 1
    while data:
        data = f.readline()
        if(data.find(word) != -1):
            print("found at", line_no)
            return
        line_no += 1
    return -1
    

print(check_for_line())


f = open("practice2.txt", "r")
data = f.read()
#this is used to split no in string
num = ""
for i in range(len(data)):
    if(data[i] == ","):
        print(int(num))
        num = ""
    else:
        num += data[i]

#this is the method for changing string into list
nums = data.split(",")
print(nums)
count = 0
for val in nums:
    if(int(val)%2 == 0):
        count += 1
print(count)
    

    














