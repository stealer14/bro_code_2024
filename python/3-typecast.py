# Typecasting is the proces of converting a variable from one
# data type to another str(), int(), float(), bool()

name = 'Bro Code'
age = 25
gpa = 3.2
is_student = True

#Get type of variable
print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

#Reassign gpa to int
gpa = int(gpa)
print(gpa)
print(type(gpa))

#Reassign age to float
age = float(age)
print(age)
print(type(age))

#Reassign age to stirng
age = str(age)
print(age)
print(type(age))