#####
#Items we cant change
#####
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")
######
bmi = round(int(int(weight)/float(height)**2),2)

if bmi < 18.5:
    print(f"Your BMI is: {bmi}.  This means you are underweight.")
elif bmi < 25:
    print(f"Your BMI is: {bmi}.  This means you are a normal weight.")
elif bmi < 30:
    print(f"Your BMI is: {bmi}.  This means you are overweight.")
elif bmi < 35:
    print(f"Your BMI is: {bmi}.  This means you are obese.")
else:
    print(f"Your BMI is: {bmi}.  This means you are clinically obese.")

print(bmi)