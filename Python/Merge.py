def msort(l):

    if len(l)<=1:
        return l
    
    n=len(l)
    M=n//2

    left=msort(l[:M])
    right=msort(l[M:])

    merged=merge(left,right)

    return merged

def merge(l1,l2):

    l3=[]
    i=0
    j=0

    while i<len(l1) and j<len(l2):
        if l1[i]<=l2[j]:
            l3.append(l1[i])
            i+=1
        else:
            l3.append(l2[j])
            j+=1   

    e1=l1[i:]
    e2=l2[j:]
    
    return l3+e1+e2

l=[1,5,2,4,3]
x=msort(l)
print(x)

    
