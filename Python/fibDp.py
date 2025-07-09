'''def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
    
print(fib(7))'''

dp=[0]*1000 
dp[1]=1

for i in range(2,len(dp)):
    dp[i]=dp[i-1]+dp[i-2]

print(dp[10])