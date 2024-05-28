#Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
#Take this opportunity to think about how you can use functions.
#Make sure to ask the user to enter the number of numbers in the sequence to generate.
n=int(input("Enter the number of sequences you want to generate:"))
n1=0
n2=1
for i in range(0,n):
    print(n1,end=" ")#end is useful!
    n3=n1+n2
    n1=n2
    n2=n3
