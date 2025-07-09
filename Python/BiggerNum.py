import random 

l=[16,17,3,4,5,2]
l2=[]

for i in range(len(l)-1):

    if l[i]<l[i+1]:
        continue
    else:
        l2.append(l[i])

l2.append(l[-1])
print(l)
print(l2)