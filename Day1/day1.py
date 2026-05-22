# name = input("Enter your name")
# age = input("Enter your age:")
# city = input("Enter your city:")

# print("Hello ",name)
# print("You are ",age ,"years old")
# print("You live in ",city)

# a = 10
# b = 3

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)
# print(a ** b)

# age = 15
# if age > 18:
#     print("Adult")
# else:
#     print("Minor")

# marks = 75
# if marks >= 90:
#     print("Grade A")
# elif marks >= 80:
#     print("Grade B")
# elif marks >= 70:
#     print("Grade C")
# else:
#     print("Grade D")


# a = input("Enter a number:")
# b = input("Enter another number:")

# if a > b:
#     print(a, "is greater than", b)
# elif a < b:
#     print(a, "is less than", b)
# else:    
#     print(a, "is equal to", b)

# a = int(input("Enter a number:"))
# if a > 0:
#     print(a, "is positive")
# elif a < 0:
#     print(a, "is negative")
# else:    print(a, "is zero")

cnt = 3

while(cnt):

    username = input("Enter your username:")
    password = input("Enter your password:")

    if username == "admin" and password == "password123":
        print("Login successful")
        break
    else:
        print("Invalid username or password")
        if cnt == 1:
            print("Too many failed attempts. Exiting.")

    cnt-=1
