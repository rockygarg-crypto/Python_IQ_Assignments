phone_num = "1234567890"
otp = "1234"
email = "user@example.com"
password = "password123"

print("LOGIN SYSTEM")
print("1.Login with phone")
print("2.Login with email")
print("3.Exit the system")

choice = int(input("Enter your choice : "))

if choice == 1:
    user_phone = input("Enter your number : ")
    user_otp = input("Enter otp : ")
    if user_phone == phone_num and user_otp == otp :
     print("Login successful")
    else:
     print("Invalid phone number or otp")
elif choice == 2:
    user_email = input("Enter your email : ")
    user_password = input("Enter your password :")
    if user_email == email and user_password == password :
        print("Login successful")
    else:
        print("Invalid email or password")
elif choice ==3:
    print("Exiting the system")
else:
    print("Invalid choice please select a valid option")

