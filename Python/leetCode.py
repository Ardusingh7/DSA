def solve(s,n,cnt):

    if n==1:
        cnt=1
        x='0'
        return x
    
    elif n==2:
        cnt=2
        x='10'
        return x
    
    elif n==cnt:
        return s
    
    else:

        y=""

        for i in s:

            if i=='0':
                y+='01'
            else:
                y+='10'

        cnt+=1
        
        return solve(y,n,cnt)
    
ans=solve('0',3,cnt=1)
print(ans)

k=int(input())
print(ans[k])