import random

l=list(range(10000))
random.shuffle(l)

n=len(l)

#Bubble sort 
for _ in range(n-1):
    for j in range(n-1):

        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]

print(l)