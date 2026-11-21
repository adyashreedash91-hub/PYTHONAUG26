# 1. Check whether a number is even or odd
# def check(num):
#     if num % 2 == 0:
#         print("Even number")
#     else:
#         print("Odd number")
# check(51)

# 2. Find the largest of three numbers

# def largest(a, b, c):
#     if a > b and a > c:
#         print(a, "is largest")
#     elif b > a and b > c:
#         print(b, "is largest")
#     else:
#         print(c, "is largest")
# largest(90, 20, 60)

# 3.Create a function to calculate factorial.
# def factorial(n):
#     fact = 1
#     for i in range(1, n + 1):
#         fact = fact * i
#     print("Factorial =", fact)
# factorial(7)

# 4.Create a function to check whether a number is prime.
# def prime(n):
#     count = 0
#     for i in range(1, n + 1):
#         if n % i == 0:
#             count = count + 1
#     if count == 2:
#         print("Prime number")
#     else:
#         print("Not a prime number")
# prime(9)

# 5.Create a function to reverse a string.
# def reverse(s):
#     print(s[::-1])
# reverse("Adya")

# 6.Create a function to calculate the sum of all elements in a list.
# def total(numbers):
#     sum = 0
#     for i in numbers:
#         sum = sum + i
#     print("Total =", sum)
# total([10, 20, 50, 90])

# 7.Create a calculator using separate functions for addition, subtraction, multiplication, and division.
# def add(a, b):
#     print("Addition =", a + b)
# def sub(a, b):
#     print("Subtraction =", a - b)
# def mul(a, b):
#     print("Multiplication =", a * b)
# def div(a, b):
#     print("Division =", a / b)

# add(10, 5)
# sub(10, 5)
# mul(10, 5)
# div(10, 5)

# 8.Create a function using args to calculate the sum of multiple numbers.
# def total(*args):
#     sum = 0
#     for i in args:
#         sum = sum + i
#     print("Total =", sum)
# total(10, 20, 50, 90, 50)

# 9.Create a function using *kwargs to display student details.
# def student(**kwargs):
#     for key, value in kwargs.items():
#         print(key, ":", value)

# student(name="Adya", age=22, city="Bhubaneswar", marks=95)

# 10.Create a recursive function to calculate the Fibonacci sequence.
