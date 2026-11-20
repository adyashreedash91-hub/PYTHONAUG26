#List
# 1.Create a list of 10 numbers and print all elements using a for loop.
# numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# for i in numbers:
#     print(i)

# 2.Write a program to print only even and odd numbers from a list.
# numbers = [10, 11, 20, 31, 40, 51, 60, 70, 81, 90]

# print("Even Numbers:")

# for i in numbers:
#     if i % 2 == 0:
#         print(i)

# print("Odd Numbers:")

# for i in numbers:
#     if i % 2 != 0:
#         print(i)

# 3.Find the largest and smallest numbers in a list using a loop.
# numbers = [10, 20, 500, 300, 111, 30, 10]

# largest = numbers[0]
# smallest = numbers[0]

# for num in numbers:
#     if num > largest:
#         largest = num

#     if num < smallest:
#         smallest = num

# print("Largest:", largest)
# print("Smallest:", smallest)

# 4.Count how many times a particular number appears in a list.
# numbers = [10, 20, 10, 30, 10, 40, 50]

# target = 10
# count = 0

# for num in numbers:
#     if num == target:
#         count += 1

# print("Number of times:", count)

# 5.Write a function to calculate the sum of all elements in a list without using sum().
# def calculate_sum(numbers):
#     total = 0

#     for num in numbers:
#         total += num

#     return total

# numbers = [10, 20, 30, 40, 50]

# print("Sum:", calculate_sum(numbers))

# 6.Find the second-largest number in a list without using sort() or max().
# numbers = [10, 20, 500, 300, 111]

# largest = numbers[0]
# second = None

# for num in numbers:
#     if num > largest:
#         second = largest
#         largest = num

#     elif num != largest:
#         if second == None or num > second:
#             second = num

# print("Second largest:", second)

# 7.Remove duplicate elements from a list without using set().
# numbers = [10, 20, 10, 30, 20, 40, 50]

# new_list = []

# for num in numbers:
#     if num not in new_list:
#         new_list = new_list + [num]

# print(new_list)

# 8.Separate positive, negative and zero values into three different lists.
# numbers = [10, -20, 0, 30, -40, 0, 50]

# positive = []
# negative = []
# zero = []

# for num in numbers:
#     if num > 0:
#         positive = positive + [num]

#     elif num < 0:
#         negative = negative + [num]

#     else:
#         zero = zero + [num]

# print("Positive numbers:", positive)
# print("Negative numbers:", negative)
# print("Zero numbers:", zero)

# 9.Find the common elements between two lists without using intersection().
# list1 = [10, 20, 30, 40, 50]
# list2 = [30, 40, 50, 60, 70]

# common = []

# for num in list1:
#     if num in list2 and num not in common:
#         common = common + [num]

# print("Common elements:", common)

# 10.Write a function to check whether a list is a palindrome.


# Tuple
# 1.Create a tuple of 10 numbers and print all elements using a for loop.
# numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

# for num in numbers:
#     print(num)

# 2.Print all elements along with their index using enumerate().
# numbers = (10, 20, 30, 40, 50)

# for index, num in enumerate(numbers):
#     print(index, num)

# 3.Find the largest and smallest numbers in a tuple using a loop.
# numbers = (10, 20, 500, 300, 111, 30)

# largest = numbers[0]
# smallest = numbers[0]

# for num in numbers:
#     if num > largest:
#         largest = num

#     if num < smallest:
#         smallest = num

# print("Largest:", largest)
# print("Smallest:", smallest)

# 4.Count how many times a particular number appears using count().
# numbers = (10, 20, 10, 30, 10, 40, 50)

# target = 10

# result = numbers.count(target)

# print("Count:", result)

# 5.Calculate the sum of all tuple elements without using sum().
# def calculate_sum(numbers):
#     total = 0

#     for num in numbers:
#         total = total + num

#     return total

# numbers = (30, 20, 60, 40, 50)

# print("Sum:", calculate_sum(numbers))

# 6.Find the second-largest number in a tuple without using sort() or max().
# numbers = (10, 20, 70000, 600, 111)

# largest = numbers[0]
# second = None

# for num in numbers:
#     if num > largest:
#         second = largest
#         largest = num

#     elif num != largest:
#         if second == None or num > second:
#             second = num

# print("Second largest:", second)

# 7.Find all duplicate elements in a tuple.
# numbers = (10, 20, 10, 30, 20, 40, 50)

# for num in numbers:
#     if numbers.count(num) > 1:
#         print(num)

# 8.Check whether a tuple is a palindrome without using slicing.


# 9.Find the common elements between two tuples using loops.
# tuple1 = (10, 20, 30, 40, 50)
# tuple2 = (30, 40, 50, 60, 70)

# common = ()

# for num in tuple1:
#     if num in tuple2 and num not in common:
#         common = common + (num,)

# print("Common elements:", common)

# 10. Separate even and odd numbers from a tuple into two different lists.
# numbers = (10, 11, 30, 31, 40, 51, 80)

# even = []
# odd = []

# for num in numbers:
#     if num % 2 == 0:
#         even = even + [num]
#     else:
#         odd = odd + [num]

# print("Even numbers:", even)
# print("Odd numbers:", odd)


# Set
# 1. Create a set of 10 numbers and print all elements using a for loop.
# numbers = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}

# for num in numbers:
#     print(num)

# 2. Create two sets and find their union.

# set1 = {10, 20, 30, 40}
# set2 = {30, 40, 50, 60}

# result = set1.union(set2)

# print("Union:", result)


# 3. Find the common elements between two sets using intersection().
# set1 = {10, 20, 30, 40}
# set2 = {30, 40, 50, 60}

# result = set1.intersection(set2)

# print("Common elements:", result)

# 4. Find the difference between two sets using difference().
# set1 = {10, 20, 30, 40}
# set2 = {30, 40, 50, 60}

# result = set1.difference(set2)

# print("Difference:", result)

# 5. Find the largest and smallest numbers in a set using a loop.
# numbers = {10, 20, 500, 300, 111, 30}

# largest = None
# smallest = None

# for num in numbers:
#     if largest == None or num > largest:
#         largest = num

#     if smallest == None or num < smallest:
#         smallest = num

# print("Largest:", largest)
# print("Smallest:", smallest)

# 6.Find common elements between two sets without using intersection().
# set1 = {10, 20, 30, 40}
# set2 = {30, 40, 50, 60}

# common = set()

# for num in set1:
#     if num in set2:
#         common.add(num)

# print("Common elements:", common)

# 7. Find the union of two sets without using union().
# set1 = {10, 20, 30, 40}
# set2 = {30, 40, 50, 60}

# result = set1.copy()

# for num in set2:
#     result.add(num)

# print("Union:", result)

# 8. Check whether two sets are equal without using the == operator.
# set1 = {10, 20, 30}
# set2 = {30, 20, 10}

# if len(set1) == len(set2) and set1.issubset(set2):
#     print("Sets are equal")
# else:
#     print("Sets are not equal")

# 9. Find the elements that are present in exactly one of three sets.
# a = {10, 20, 30}
# b = {20, 30, 40}
# c = {30, 40, 50}

# result = set()

# for i in a | b | c:
#     count = 0

#     if i in a:
#         count += 1

#     if i in b:
#         count += 1

#     if i in c:
#         count += 1

#     if count == 1:
#         result.add(i)

# print(result)

# 10.Find the common characters between two strings using sets.
# a = "Rama"
# b = "Hari"

# s1 = set(a)
# s2 = set(b)

# result = set()

# for i in s1:
#     if i in s2:
#         result.add(i)

# print("Common characters:", result)

# dictionary

# 1. Create a dictionary containing 5 students and their marks. Print all keys and values using a loop.
# students = {
#     "Adya": 80,
#     "Amit": 90,
#     "Arav": 70,
#     "Riya": 85,
#     "Sneha": 95
# }

# print("Student Names:")

# for key in students.keys():
#     print(key)

# print("Student Marks:")

# for value in students.values():
#     print(value)

# 2. Add a new key called city to an existing dictionary.
# student = {
#     "name": "Adya",
#     "age": 21,
#     "marks": 85
# }

# student["city"] = "Bhubaneswar"

# print(student)

# 3. Update the marks of a particular student.
# students = {
#     "Adya": 80,
#     "Aani": 90,
#     "Amit": 70
# }

# students["Rahul"] = 95

# print(students)

# 4. Find the total marks of all students without using sum().
# students = {
#     "Rahul": 80,
#     "Priya": 90,
#     "Amit": 70,
#     "Riya": 85,
#     "Sneha": 95
# }

# total = 0

# for marks in students.values():
#     total = total + marks

# print("Total marks:", total)

# 5. Count how many students passed and failed. Consider 40 as the passing mark.
# students = {
#     "Adya": 80,
#     "Priyanka": 35,
#     "Aarav": 70,
#     "Riya": 25,
#     "Sneha": 95
# }

# pass_count = 0
# fail_count = 0

# for marks in students.values():
#     if marks >= 40:
#         pass_count += 1
#     else:
#         fail_count += 1

# print("Passed:", pass_count)
# print("Failed:", fail_count)

# 6. Find the student with the highest and lowest marks without using max() or min().
# students = {
#     "Adya": 80,
#     "Priyanka": 90,
#     "Aarav": 70,
#     "dipa": 85,
#     "Sneha": 95
# }

# highest = 0
# lowest = 100

# high_name = ""
# low_name = ""

# for name, marks in students.items():

#     if marks > highest:
#         highest = marks
#         high_name = name

#     if marks < lowest:
#         lowest = marks
#         low_name = name

# print("Highest:", high_name, highest)
# print("Lowest:", low_name, lowest)

# 7. Find the second-highest marks from a student dictionary.
# students = {
#     "Adya": 80,
#     "Priyanka": 90,
#     "Aarav": 70,
#     "Bipin": 85,
#     "Sneha": 95
# }

# first = 0
# second = 0

# for marks in students.values():

#     if marks > first:
#         second = first
#         first = marks

#     elif marks > second and marks != first:
#         second = marks

# print("Second highest marks:", second)

# 8. Create a new dictionary containing only students who scored more than 75.
# students = {
#     "Adya": 80,
#     "Priyanka": 90,
#     "Aara": 70,
#     "Bipin": 60,
#     "Sneha": 95
# }

# new_dict = {}

# for name, marks in students.items():
#     if marks > 75:
#         new_dict[name] = marks

# print(new_dict)

# 9. Find the frequency of each character in a string and store it in a dictionary.



# 10. Merge two dictionaries without using the update() method.
# a = {
#     "name": "Rahul",
#     "age": 21
# }

# b = {
#     "city": "Bhubaneswar",
#     "marks": 90
# }

# for key, value in b.items():
#     a[key] = value

# print(a)