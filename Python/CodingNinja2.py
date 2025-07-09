from bisect import bisect_left

def BinarySearch(a, x):
    i = bisect_left(a, x)
    if i:
        return (i-1)
    else:
        return -1
 
def findMaximumBefore(arr, n):
 
    res = [-1] * (n + 1)
     
    lst = []
    lst.append(arr[0])
 
    for i in range(1, n):
        idx = BinarySearch(lst, arr[i])
        if(idx != -1):
            res[i] = lst[idx]
 
        lst.insert(idx+1 , arr[i])
 
    res.pop()
    print(res)

    
arr = [34,5,29,13,43,6,36,35,2,25,37,2,33,17,6,18,42,1,26,6,22,10,18 ,39 ,30 ,48 ,3 ,40, 8, 41, 48, 33, 25, 21, 2, 21, 25,22, 15, 49, 10, 22, 7 ,47 ,47, 3 ,8 ,8 ,14]
n = len(arr)
findMaximumBefore(arr, n)