r=int(input())
k=0

for i in range(1,r+1):
    for j in range(1,r-i+1):
        print(end="  ")
    while k!=2*i-1:
        print("* ",end="")
        k+=1
    k=0
    print()

l=input('')
a=l.split(' ')
print(a)
b=list(map(int,a))
print(b)
