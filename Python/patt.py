def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)

l=[]
s=0

for i in range(5):
    l.append(fib(i))
    print(fib(i))
    s=+fib(i)

print(l)
print(s)

for i in l:
    if i%2!=0:
        print(i)
