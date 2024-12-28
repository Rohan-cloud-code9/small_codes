#dictionary
info = {
    "name" : "rohan pandey",
    "sisters" : ["ruvi", "vaishnavi"],
    "subject" : ("maths", "physics"),
    "marks" : 97.6,
}
print(info)
print(info["name"])
print(info["sisters"])
print(info["subject"])
print(info["marks"])

info["name"] = "aishwarya"
info["surname"] = "pandey"
print(info)

#nested dictionary

student = {
    "name" : "rohan pandey",
    "subjects" : {"physics" : 56,
                  "chem" : 67,
                  "maths" : 56},
    "age" : 19
}
print(student)
print(student["subjects"]["maths"])

print(list(student.keys()))
print(list(student.values()))
print(len(student))
print(list(student.items()))
print(student.get("age"))
student.update({"city" : "uttar pradesh"})
print(student)

#sets
collection = {1, 2, 2, 4, "hello", "world"}
print(collection)
print(len(collection))

null_dict = {} #empty dictionary
print(type(null_dict))

#for empty set
null_set = set()
print(type(null_set))

relation = {1, 2, 3}
relation.add(4)
relation.remove(3)
print(relation)
relation.clear()
print(relation)

set_1 = {"hello", "pyhton", "coding", "school", "rakesh"}
print(set_1.pop())
print(set_1.pop())

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1.union(set2))
print(set1.intersection(set2))

#practice
dict_2 = {
        "table" : ["a piece of furniture", "list of facts and figures"],
         "cat" : "a small animal"}
print(dict_2)

set_class = {"python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "C"}
print("Nmuber of classrooms required are " , len(set_class))

#practice
exam_marks = {}
subject1 = int(input("enter your marks in physics : "))
subject2 = int(input("enter your marks in maths : "))
subject3 = int(input("enter your marks in chemistry : "))
exam_marks.update({"physics" : subject1})
exam_marks.update({"maths" : subject2})
exam_marks.update({"chemistry" : subject3})
print(exam_marks)

set_9 = set()
set_9.add("9")
set_9.add("9.0")
print(set_9)