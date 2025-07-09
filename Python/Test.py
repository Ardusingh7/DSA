import random 
import time

def merged(l):

    if len(l)<=1:
        return l
    
    mid=len(l)//2 
    left=l[:mid]
    right=l[mid:]

    lefts,rights=merged(left),merged(right)

    return merge(lefts,rights)

def merge(lefts,rights):

    i=0
    j=0
    dummy=[]

    while i<len(lefts) and j<len(rights):
        if lefts[i]<=rights[j]:
            dummy.append(lefts[i])
            i+=1
        else:
            dummy.append(rights[j])
            j+=1

    e1=lefts[i:]
    e2=rights[j:]

    return dummy+e1+e2

l=list(range(100))
random.shuffle(l)
#print(l)
start=time.time()
#print(merged(l))
merged(l)
end=time.time()
print("Time to merge: ", end-start)