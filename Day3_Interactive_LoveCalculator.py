print("Welcome to the Love Calculator")
name1 = input("What is your name: ").lower()
name2 = input("What is their name: ").lower()

combined_names = name1 + name2
t = combined_names.count('t')
r = combined_names.count('r')
u = combined_names.count('u')
e = combined_names.count('e')
l = combined_names.count('l')
o = combined_names.count('o')
v = combined_names.count('v')


true_count = t + r + u + e
love_count = l + o + v + e

love_score = str(true_count)+str(love_count)
love_score = int(love_score)
print(f"Your love score is: {love_score}")

if love_score < 10 or love_score > 90:
    print(
        f"Your love score is {love_score}, you go together like coke and mentos")
elif love_score >= 40 and love_score <= 50:
    print(f"Your love score is {love_score}, you are alright together")
else:
    print(f"Your love score is {love_score}")
