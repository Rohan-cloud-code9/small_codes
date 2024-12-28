student = ["rohan", 97.6, 19, "jalalpur"]
print(student)
print(student[0])
print(student[1])
print(student[2])
print(student[3])
student[1] = 100
print(student)

#sublist
marks = [97, 80, 56, 76, 86]
print(marks[:5])
print(marks[0:])
print(marks[1:4])
print(marks[-3:-1])


#list methods
list = [1, 3, 2, 4]
list.append(5)
print(list)
list.sort()
print(list)
list.sort(reverse= True)
print(list)
list.reverse()
print(list)
list.insert(1, 6)
print(list)
list.remove(6)
list.pop(4)
print(list)
print(len(list))


#tuples
tup = (1, 2, 3, 5)
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup)

#methods
TUP = (2, 1, 3, 1)
print(TUP.index(1))
print(TUP.count(1))

#practice
 
Fav_movies = []
print("Can you tell us your top 3 favourite movies")
movie_1 = input("movie1 : ")
movie_2  = input("movie2 : ")
movie_3 = input("movie3 : ")
Fav_movies.append(movie_1)
Fav_movies.append(movie_2)
Fav_movies.append(movie_3)
print(Fav_movies)


list_1 = [1, 2, 1]
list_2 = [1, 2, 3]

copy_list_1 = list_1.copy()
copy_list_1.reverse()
if(copy_list_1 == list_1):
    print("palindrome")
else:
    print("not palindrome")

copy_list_2 = list_2.copy()
copy_list_2.reverse()
if(copy_list_2 == list_2):
    print("palindrome")
else:
    print("not palindrome")

tup_1 = ('C', 'D', 'A', 'A', 'B', 'B', 'A' )
print(tup_1.count('A'))

List_1 = ['C', 'D', 'A', 'A', 'B', 'B', 'A' ]
List_1.sort()
print(List_1)




