# Student Registration Status Checker in Python

stu_name = str(input("Enter your name: "))
units = int(input("Enter no. of units registered: "))

response = f"Student Name: {stu_name.capitalize()}\nUnits Registered: {units}\nStatus: {'Overload - Approval Required.' if units > 7 else 'Registration Accepted.'}"


if units > 7:
    print("-"*30)
    print(response)
    print("-"*30)
else:
    print("-"*30)
    print(response)
    print("-"*30)