# eCitizen Login Validation System in Python

username = str(input("Enter your username: "))
password = str(input("Enter your password: "))

if username == "adminKE" and password == "254Secure":
    print("\nAccess Granted.")
else:
    print("\nAccess Denied. Invalid Credentials.")