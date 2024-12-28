#RANDOM PAssword generator
import random
import string

character_values = string.ascii_letters + string.digits + string.punctuation
pass_len = 8
password = ""
for i in range(pass_len):
    password += random.choice(character_values)

print("your random password is : " , password)

#second method
password1 = "".join(random.choice(character_values) for i in range(pass_len))
print(password1)
