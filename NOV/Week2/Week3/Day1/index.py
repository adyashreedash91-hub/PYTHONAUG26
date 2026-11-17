#List
# fruits = ["Apple","orange","fruit1"]

# for i, fruit in enumerate (fruits):
#     print(i+1,fruit)

# Tuple
# fruits =( "Apple","orange","fruit1")

# for i, fruit in enumerate (fruits):
#     print(i+1,fruit)


#Set
# fruits = {"Apple","orange","fruit1"}

# for i, fruit in enumerate (fruits):
#     print(i+1,fruit)

#Dict
# students = {
#     "name":"Rahul",
#     "age" : "22",
#     "city" : "bbsr",
# }
# for key ,val in students.items():
#     print(key,'is' ,val)


# Function
#simple fumction

# def welcome():
#     print("welcome to python")

# welcome()

#Argument
# positional argument
# def welcome_with_name(name, age, city):
#     print("welcome", name)
#     print("welcome", age)
#     print("welcome", city)

# welcome_with_name("adya", 22, "BBSR")

#Keyword argument


#default argument


#variable lenth agrument



# local scope, global scope



# Return
# def welcome():
#     return "welcome to python"

# res = welcome()
# print(res)


# write a function  with a arg that return number is even or odd
# def check_even_odd(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"

# res = check_even_odd(20)
# print(res)

# 2.wwrite a function that take a list of numbers and return the largest number
# numbers = [10,20,500,300,1111]

# def largest_number(numbers):
#     largest = numbers[0]

#     for num in numbers:
#         if num > largest:
#             largest = num

#     return largest

# numbers = [10, 20, 500, 300, 1111,500,200]

# print("Largest number:", largest_number(numbers))

# 3.write a function that takes a list of numbers and return largest and smallest numbers
# numbers = [10,20,500,300,111,30,10]


# def find_largest_smallest(numbers):
#     largest = numbers[0]
#     smallest = numbers[0]

#     for num in numbers:
#         if num > largest:
#             largest = num

#         if num < smallest:
#             smallest = num

#     return largest, smallest


# largest, smallest = find_largest_smallest(numbers)

# print("Largest:", largest)
# print("Smallest:", smallest)

# 4.write a function that take a age and return voting Eligibility
# not Eligibile
# Eligibile
# just-18

# def voting(age):
#     if age < 18:
#         return "Not Eligible"
#     elif age == 18:
#         return "Just-18"
#     else:
#         return "Eligible"

# print(voting(16))
# print(voting(18))
# print(voting(20))

# 5.write a function that takes mark and show Grade
# mark     Grade
# 90-100 ->A
# 80-89  ->B
# 78-79  ->C
# 50-59  ->D
# less the 50 -> fail

# def show_grade(mark):
#     if mark >= 90 and mark <= 100:
#         print("A")
#     elif mark >= 80 and mark <= 89:
#         print("B")
#     elif mark >= 78 and mark <= 79:
#         print("C")
#     elif mark >= 50 and mark <= 59:
#         print("D")
#     else:
#         print("Fail")


# show_grade(95)
# show_grade(85)
# show_grade(78)
# show_grade(55)
# show_grade(40)


# 6.write the function that takes a number list and show the numbers are even or odd
# numbers = [10,11,530,320,111,30,10]

# 10-even
# 11-odd
# 530-even
# 320-even
# 111-odd
# 30-even
# 10-odd

# def check_even_odd(numbers):
#     result = []
#     for num in numbers:
#         if num % 2 == 0:
#             result.append(str(num) + "-even")
#         else:
#             result.append(str(num) + "-odd")
#     return result


# numbers = [10, 11, 530, 320, 111, 30, 10]

# print(check_even_odd(numbers))

# 7.write the function that takes a number list and show how many even and odd are there
# numbers = [10,11,530,320,111,30,10]
# odd numbers are 2 and even numbers are 5

# def count_even_odd(numbers):
#     even = 0
#     odd = 0

#     for num in numbers:
#         if num % 2 == 0:
#             even += 1
#         else:
#             odd += 1

#     return even, odd


# numbers = [10, 11, 530, 320, 111, 30, 10]

# even, odd = count_even_odd(numbers)

# print("Odd numbers are", odd)
# print("Even numbers are", even)

# 8. write a function with n as arg, that show the multiplication table 
# n=5
# def multiplication(n):
#     for i in range(1, 11):
#         print(n, "x", i, "=", n * i)


# multiplication(7)