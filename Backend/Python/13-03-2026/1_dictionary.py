#Dictionary Properties:
# Ordered, Mutable(Changeable), Duplicate Values not allowed
student = {
    "name" : "Preetham B N",
    "College" : "AIEMS",
    "degree" : "BE",
    "branch" : "CSE",
    "sem" : 8,
    "hobbies" : ["Singing", "Playing", "Gaming", "Learning"]
}
print(student)
print(type(student))

print("Student Name :", student["name"])
print("Student Hobbies :", student["hobbies"])

#Dictionary Methods:
#keys, values, items, get, pop, popitem, update, copy, clear

#keys
print(student.keys())

#values
print(student.values())

#items
print(student.items())

#get
print(student.get("name"))

#update
student.update({"skills" : ("HTML", "CSS", "Bootstrap", "JavaScript")})
print(student)

student.update({"College" : "ParvaM"})
print(student)

#pop
student.pop("sem")
print(student)

#popitem
student.popitem()
print("Student Details: ", student)

#copy
new_student = student.copy()
print(new_student)

#clear
new_student.clear()
print(new_student)