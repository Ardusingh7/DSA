a=[1,1,1,2,2,2,3,3,3]
b=[1,1,1,2,2,2]

a1=sorted(set(a))
b1=sorted(set(b))

def check():
    for i in b1:
        if b.count(i)!=a.count(i):
            return False
        
    return True

print(check())