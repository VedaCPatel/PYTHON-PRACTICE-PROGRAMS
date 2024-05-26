'''write a program that prints out all the elements of the list that are less than 50.'''
n=1
l1=[]
while n<6:
    num = int(input("Type integer no."+str(n)+" :"))
    a=num
    b=l1.append(a)
    n+=1
print("The list of integers you provided is:",l1)
l2=[]
d=0
for i in l1:
    if i<50:
        c=l2.append(i)
        d+=1
if d==5:
    print("All the integers are lesser than 50!")
elif d==0:
    print("There are no integers lesser than 50 in the above list!")
else:
     print(l2, "is the list of numbers lesser than 50!")






