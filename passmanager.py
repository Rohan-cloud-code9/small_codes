def Add():
    name = input("acoount name - ")
    password = input("password - ")
    with open("passwords.txt", "a") as f:
        f.write(name + "|" + password +"\n")

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, password = data.split("|")
            print("User-", user,"|" ,"Password-", password)
        
    
mas_pass = input("please enter the master password to access your passwords-")
if(mas_pass == "DIGNIFY@321"):
    pass
else:
    print("incorrect password")
    quit()
    

while True:
    mode = input("whould you like to add or view the passwords or press q to exit(add/view/q)--").lower()
    if mode == "q":
        break
    if mode == "add":
        Add()
    elif mode == "view":
        view()
    else:
        print("not a valid command")
        continue
    

        














