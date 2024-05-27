#Ask the user for a number and determine whether the number is prime or not.
n=int(input("Enter a number:"))
p=[]
for i in range(1,n):
    if n%i==0:
        P=p.append(i)
Pa=len(p)
if Pa==1:
    print(n,"is a prime number!")
else:
    print(n,"is not a prime number!")


