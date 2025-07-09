n = 7
num=1
s=0
for i in range(0, n):
        curr=1
        for j in range(0, i+1):
            curr=curr*num
            num = num + 1
        s+=curr 
print(s%(10**9+7))
