#code

n=int(input())

l=[]

for i in range(n):
    
    l.append(input())
    
flag1=False
flag2=False

for i in l:
    
    y=len(i)

    for j in range(y):

        if i[j].isdigit():
            flag1=True
        elif i[j].islower():
            flag2=True
            
    if flag1==True and flag2==True:
        print("YES")
    else:
        print("NO")
            