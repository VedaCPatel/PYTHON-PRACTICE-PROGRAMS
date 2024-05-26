#Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)
input=input("Enter any string:")
rev=input[::-1] #Used to reverse a string
if rev==input:
    print("The string is a palindrome!")
else:
    print("The string is not a palindrome!")




