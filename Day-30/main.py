# try:
#     file = open("a_file.txt")
#     a_dict = {"Key1": "Value1"}
#     print(a_dict['Key1'])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Created in except block")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print(f"{file.name} was closed")
#     raise TypeError("YOU DONE MESSED UP!")

# height = float(input("Height: "))
# weight = float(input("Weight: "))
#
# if height > 3:
#     raise ValueError(f"{height} is not a real value, should not be over 3")
# bmi = weight / height ** 2
# print(bmi)


# Day 30.1 Coding Exercise
# fruits = ["Apple", "Pear", "Orange"]
#
# TODO: Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit Pie")
#     else:
#         print(fruit + " pie")
#
#
# make_pie(4)
#

# Day 30.2 Coding Exercise
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        total_likes += 0
        # Or we can pass


print(total_likes)