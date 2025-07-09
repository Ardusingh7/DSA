def ques():
    try:
        f=open('Gay.txt','r')
        print(f.read())
    except FileNotFoundError:
        print('Kya kr rha hai Bhai?')

    l=[1,2,3,4,5]
    for i, j in enumerate(l):
        if i%2!=0:
            print(["index",i,"value",j])

    n=int(input())
    l1=[n*i for i in range(1,11)]
    print(l1)

    try:
        a=int(input())
        b=int(input())
        print(a/b)
    except ZeroDivisionError:
        print("Infinity!")

print('-------------------------------------------------')

n=1
for i in range(5):
    for j in range(i+1):
        print(n,end=' ')
        n+=1
    print()

for i in range(65,70):
    for j in range(65,i+1):
        print(chr(j),end=' ')
    print()

print('-------------------------------------------------')

def fact(n):
    if n==1:
        return n
    else:
        return n * fact(n-1)

print(fact(5))

print('-------------------------------------------------')

def feb_se(n):
    if n<=1:
        return n
    else:
        return feb_se(n-1) + feb_se(n-2)

for i in range(5):
    print(feb_se(i))
    
print('-------------------------------------------------')

n=1234
t=n
r=0

while n>0:

    d=n%10
    r=r*10 + d
    n=n//10

print(t,r)

print('-------------------------------------------------')

def sum_no(n):

    if n==0:
        return n
    else:
        return n%10 + sum_no(n//10)

print(sum_no(1234))

print('-------------------------------------------------')

def rev_no(n,r):
    if n==0:
        return r
    else:
        return rev_no(n//10, r*10 + n%10)
    
print(rev_no(1234,0))

print('-------------------------------------------------')

s= lambda x,y: x+y
print(s(7,10))

print('-------------------------------------------------')

def cube(n):
    return n**3

l=[1,2,3,4,5]
print(list(map(cube,l)))

print('-------------------------------------------------')






    


