# Typical for loop with lists:
numbers = [1, 2, 3]
new_list = []

for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

# Our list comprehension would be:
new_comp = [n + 1 for n in numbers]

# Can be used with strings also
name = "Mike"
letter_name = [letter for letter in name]

# Challenge!  Using range(1,5) use a list comprehension to double the numbers in the list
doubled_num = [n * 2 for n in range(1, 5)]

# Conditional list comprehensions, add short names to a list (less than 4 letters)
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_name = [name for name in names if len(name) < 5]
# Take all names greater than 5 and make all letters uppercase
uppercase_name = [name.upper() for name in names if len(name) > 5]

# Squared numbers!
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n ** 2 for n in numbers]

# Filtering even numbers!
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
even_numbers = [num for num in numbers if num % 2 == 0]

# Data Overlap
# with open('file1.txt') as f:
#     file_1_list = f.readlines()
#     file_1 = [int(i.replace("\n", "")) for i in file_1_list]
# with open('file2.txt') as f:
#     file_2_list = f.readlines()
#     file_2 = [int(i.replace("\n", "")) for i in file_2_list]

# def readfile(file):
#     with open(file) as f_open:
#         f_read = f_open.readlines()
#         f = [int(i.replace("\n", "")) for i in f_read]
#     return f
# file_1 = readfile("file1.txt")
# file_2 = readfile("file2.txt")

# with open('file1.txt') as f:
#     file_1 = f.readlines()
# with open('file2.txt') as f:
#     file_2 = f.readlines()
#
# result = [int(num) for num in file_1 if num in file_2]
# print(result)

#### Dictionary Comprehensions
import random
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
students_scores = {student: random.randint(1, 100) for student in names}


# Find passing students (greater than 60)
passed_students = {student: score for (student, score) in students_scores.items() if score >= 60}


# Dictionary Comprehension Coding Challenge 1
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word: len(word) for word in sentence.split()}


# Dictionary Comprehension Coding Challenge 2
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {day: (temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}

# Iterating over a Pandas Dataframe
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
import pandas as pd

student_df = pd.DataFrame(student_dict)

for (index, row) in student_df.iterrows():
    print(row.student)