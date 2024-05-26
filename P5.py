#write a program that returns a list that contains only the elements that are common between the
#lists (without duplicates).Make sure your program works on two lists of different sizes.

l1=[1,3,4,5,7,11,9,4]
l2=[1,4,7,8,11,10,23,4]
l3=[]
a=1
b=1
max=0
min=0
for i in l1:
    a+=1
for j in l2:
    b+=1
if a<b:
    max=set(l2)#set() method is used to remove duplicates in a list
    min=set(l1)
else:
    max=set(l1)
    min=set(l2)

for k in max:
    for l in min:
        if k==l:
            l3.append(k)
print(l3)



