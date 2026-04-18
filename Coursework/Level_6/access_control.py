def check_access(role):
    if role != "Doctor":
        raise Exception("Only Doctors are allowed.")
    else:
        print("Access Granted.")

employee_role = input("Enter your role: ")
check_access(employee_role)