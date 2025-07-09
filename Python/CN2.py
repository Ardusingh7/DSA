arr=[-7, 1, 5, 2, -4, 3, 0]

s=sum(arr)
x=arr[0]
s-=x
        
flag=False
        
for i in range(1,len(arr)):
    s-=arr[i]
    if x==s:
        flag=i
        break
    else:
        x+=arr[i]
        #print(s,x)

if flag==False:
    print(-1)
else:
    print(flag)