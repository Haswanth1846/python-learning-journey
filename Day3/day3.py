# for i in range(5):
#     print(i)

# for i in range(1, 10, 2):
#     print(i)

# name = "Haswanth"
# for ch in name:
#     print(ch)

# numbers = [1, 2, 3, 4, 5]
# for n in numbers:
#     print(n)

# cnt = 1
# while cnt < 5:
#     print("Count is ", cnt)
#     cnt += 1


# for i in range(1,101):
#     print(i)

# for i in range(1, 51):
#     if(i %2 == 0):
#         print(i)


# sum = 0
# for i in range(1,101):
#     sum+=i
#     print(sum)


# string = input("Enter a string:")
# for ch in string:
#     if ch in "aeiouAEIOU":
#         print(ch, "is a vowel")
#     else:
#         print(ch, "is a consonant")

# table = int(input("Enter a number:"))
# for i in range(1, 11):
#     print(table, "x", i, "=", table*i)

# guess = 7
# while True:
#     num = int(input("Enter a number:"))
#     if num == guess:
#         print("Congratulations! You guessed the number.")
#         break
#     else:
#         print("Try again!")


# def greet(name):
#     print("Hello, " + name + "! Welcome to the program.")


# greet("Haswanth")

# def add(a,b):
#     return a+b


# print(add(5, 3))


# def even_or_odd(num):
#     if num %2 == 0:
#         return "Even"
#     else:        return "Odd"


# print(even_or_odd(10))
# print(even_or_odd(7))



# def countVowels(string):
#     vowels = 0
#     for ch in string:
#         if ch in "aeiouAEIOU":
#             vowels += 1
#     return vowels

# string = input("Enter a string:")
# vowels = 0

# print(countVowels(string))

# def largestAmong3(a,b,c):
#     if a >= b and a >=c:
#         return a
#     elif b >= a and b >= c:
#         return b    
#     else:        return c


# a = int(input("Enter first number:"))
# b = int(input("Enter second number:"))  
# c = int(input("Enter third number:"))
# print("The largest number is:", largestAmong3(a,b,c))



def calculate(a,b,choice):
    if choice == 1:
        return a + b
    elif choice == 2:
        return a - b
    elif choice == 3:
        return a * b
    elif choice == 4:
        if b != 0:
            return a / b
        else:            return "Error: Division by zero"
    else:        return "Invalid choice"
    
a = int(input("Enter a number:"))
b = int(input("Enter another number:"))
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice:"))
print(calculate(a,b,choice))