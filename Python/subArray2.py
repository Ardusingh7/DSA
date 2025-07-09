#Input : Arr[] = { 1 , 2 , 3 , 4 , 5 , 5  }
#Output :  { 1 2 3 4 } { 5 , 5 }

arr= [1 , 2 , 3 , 4 , 5]

def equalSub(arr):

    ls= 0
    rs= sum(arr)

    for i in range(len(arr)):

        if ls==rs:
            return (arr[:i], arr[i:])
        else:
            x=arr[i]
            ls+=x
            rs-=x
        
    return "None possible!"

ans= equalSub(arr)
print(ans)
