#Input: arr[] = {1, 4, 2, 10, 2, 3, 1, 0, 20}
#k = 4, sum = 18
#Output: YES

arr= [1, 4, 2, 10, 2, 3, 1, 0, 20]
k=4
sm=0

n=len(arr)

for i in range(0,k):
    sm+=arr[i]

s=0 
e=k

maxS=sm

while e<n:

    cs= sm-arr[s]+arr[k]
    s+=1
    e+=1

    maxS=max(maxS, cs)

print(maxS)