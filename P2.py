#Ask the user for a number.
# Depending on whether the number is even or odd, print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?
num=int(input("Enter a number:"))
if num%4==0:
    print("The number is a multiple of four!")
elif num%2==0:
    print("The number is even!")
else:
    print("The number is odd!")

