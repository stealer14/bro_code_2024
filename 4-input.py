# Chapter 4 User input

# input() is a function that prompts the user to enter data
# returns the entered ata as a string

name = input("What is your name?: ")
age = input("How old are you?: ")

age = int(age)
age  = age + 1

print(f"Hello, {name}")
print("Happy Birthday!")
print(f"You are {age} years old")
