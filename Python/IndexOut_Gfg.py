l=[1,3,5,8,9,2,6,7,6,8,9]

i=0
cnt=0

for _ in l:
    
    if i>len(l)-1:
        #cnt+=1
        break
    elif i==len(l)-1:
        break
    
    else:
        i=l[i]+i
        cnt+=1
        print(i)

print(cnt)