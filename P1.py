# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old
name = input("Enter your name:")
age = int(input("Enter your age:"))
gen=input("Male or Female?:")
result = 2024+(100-age)
Male=("Male","male","M","m")
Female=("Female","female","F","f")
for g in Male:
    if gen==g:
        print(name, "will become a 100 years old in the year:", result,"👴")


for G in Female:
    if gen==G:
        print(name, "will become a 100 years old in the year:", result,"👵")








