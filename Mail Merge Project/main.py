# letter = open('./Input/Letters/starting_letter.txt', mode='r')
# letter_open = letter.read()
#
# with open("./Input/Names/invited_names.txt", mode='r') as data:
#     for n in data:
#         name = n.strip()
#         with open("./Output/ReadyToSend/letter_for_"+name+".txt", mode='w') as new_file:
#             new_file.write(letter_open.replace("[name]", name))
# letter.close()

# Angela's Way
PLACEHOLDER = "[name]"

with open('./Input/Names/invited_names.txt') as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode='w') as completed:
            completed.write(new_letter)
