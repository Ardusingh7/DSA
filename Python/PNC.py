import time
from collections import deque

l=list(range(1,100000))

s=time.time()
def sol(arr,k):

    l2=[]
    ind=0
    #d=deque(l)
    
    while l:
        ind=(ind+k-1)%len(l)
        l2.append(l[ind])
        l.pop(ind)

    return l2[-1]

print(sol(l,3))
f=time.time()
print("time taken: ",f-s)