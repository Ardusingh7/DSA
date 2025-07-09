import time

l=[True for i in range(111)]

s=time.time()

p=2

while p*p<=110:
    if l[p]==True:
        for i in range(p*p,111,p):
            l[i]=False
    p+=1    


cnt=0

for i in range(100,110):
    if l[i]:
        cnt+=1
f=time.time()
print(cnt)
print("time: ",f-s)