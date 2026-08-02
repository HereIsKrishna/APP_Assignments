# Assignment 0: 
# Develop a Python Program that demonstrates the use of 
# required, keyword, default, and variable-length arguments through functions.

# Function with required argument
def student_required(name, roll_no):
    print("Student Name:", name)
    print("Roll No:", roll_no)


# Function with keyword argument
def student_keyword(name, roll_no):
    print("Student Name:", name)
    print("Roll No:", roll_no)


# Function with default argument
def student_default(name, roll_no, room="SY4"):
    print("Student Name:", name)
    print("Roll No:", roll_no)
    print("Student Class:", room)


# Function with variable length argument
def student_length(*subject):
    print("Favourite Subjects:", subject)


# Calling function using required argument
name = input("Enter student name: ")
roll_no = int(input("Enter roll number: "))
student_required(name, roll_no)


# Calling function using keyword argument
name = input("\nEnter student name: ")
roll_no = int(input("Enter roll number: "))
student_keyword(name=name, roll_no=roll_no)


# Calling function using default argument
name = input("\nEnter student name: ")
roll_no = int(input("Enter roll number: "))
room = input("Enter student class: ")
student_default(name, roll_no, room)


# Calling function using variable length argument
sub1 = input("\nEnter first favourite subject: ")
sub2 = input("Enter second favourite subject: ")
sub3 = input("Enter third favourite subject: ")
student_length(sub1, sub2, sub3)