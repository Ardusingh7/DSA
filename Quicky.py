def part(arr,l,h):

    pivot= arr[h]
    i=l-1

    for j in range(l,h):

        if arr[j]<=pivot:
            i+=1

            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[h]=arr[h],arr[i+1]

    return i+1

def quicky(arr,l,h):

    if l<h:

        pi=part(arr,l,h)

        quicky(arr,l,pi-1)
        quicky(arr,pi+1,h)

l=[9,1,8,2,7,6,3,4]

n=len(l)

quicky(l,0,n-1)
print(l)