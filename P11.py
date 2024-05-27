#Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
#and makes a new list of only the first and last elements of the given list.
import random
l=[]
for i in range(0,5):
    a=random.randint(0,1000)
    b=l.append(a)
print("The initial list is:",l)
L=[]
c=L.append(l[0])
c=L.append(l[4])
print("The final list is:",L)


