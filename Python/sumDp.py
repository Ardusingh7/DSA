arr=[1,2,3,4,5,6,7,8,9,10]

def solve(arr,n,capacity):

    dp={}   
    if capacity == 0:
        return 1
    elif n==0:
        return 0
    elif (n,capacity) in dp:
        return dp[(n,capacity)]
    else:

        item=arr[n-1]
        if item <=capacity:

            c1=solve(arr,n-1,capacity-item)
            c2=solve(arr,n-1,capacity)

            c=c1 or c2
        
        else:
            c=solve(arr,n-1,capacity)
        dp[(n,capacity)]=c

    return c

print(solve(arr,5,9))


