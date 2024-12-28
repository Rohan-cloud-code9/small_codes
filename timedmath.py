import time
import random

operators = ["+", "-", "*"]


def generate_problems():
    sign = random.choice(operators)
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    problem = str(num1) + sign +  str(num2)
    solution = eval(str(problem))
    return problem , solution


no_of_probl = 10
correct = 0
incorrect = 0
not_attempted = 0
input("Press enter to start !")
print("---------------------")
start_time = time.time()

for i in range(no_of_probl):
    problem, solution = generate_problems()
    guess = input("problem #" + str(i +1) + ": " + problem + " = ")
    if(guess == str(solution)):
        correct += 1
    elif(guess == ""):
        not_attempted += 1
    else:
        incorrect += 1
end_time = time.time()

print("\ncorrect answers -", correct)
print("incorrect answers -", incorrect)
print("not attempted", not_attempted)
timer = int(end_time-start_time)
print("time taken to finish the test" , timer, "seconds" )
print("---------------------")
print("Nice work!!!")

    







