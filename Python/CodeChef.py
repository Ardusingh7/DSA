import math

n=int(input())

for i in range(n):
    
    l=list(map(int,input().split()))
    #print(l)
        
    t=math.ceil(l[0]/l[1])
    h=math.ceil(l[0]/l[2])
    #print(t)
    #print(h)
        
    if(t-h==1):
        print(0)
    elif(t-h>=2):
        print(t-h-1)
    elif(h==t):
        print(-1)
        
    