l=[0 for i in range(5)]
l[0]=0
l[1]=1
        
for i in range(2,5):
    l[i]=l[i-1]+l[i-2]
    
for i in range(len(l)):
    print(l[i],end=' ')


            