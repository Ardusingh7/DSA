import random

l=list(range(0,25))
random.shuffle(l)
print(l)

n=len(l)

for _ in range(n-1):
    for j in range(n-1):

        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]

print(l)