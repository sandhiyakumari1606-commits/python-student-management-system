print("STUDENT MANAGEMENT SYSTEM ")
name=input("Enter student name:")
age=input("Enter student age:")
course=input("Enter student course:")
print("\n---Students Details---")
print("Name:",name)
print ("Age:",age)
print ("Course:",course)
students=[]
students.append({
"name":name,
"age":age,
"course":course
})
print ("\n Student added successfully!")