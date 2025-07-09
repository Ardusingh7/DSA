r=int(input('rows'))
n=1

for i in range(r):
    for j in range(i+1):
        print(n,end=' ')
        n+=1
    print()

