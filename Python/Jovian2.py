#Merge sort

import random

def merging(nums):

    if len(nums)<=1:
        return nums
    
    mid=len(nums)//2
    left=nums[:mid]
    right=nums[mid:]

    lefts=merging(left)
    rights=merging(right)

    merge_=merge(lefts,rights)

    return merge_

def merge(nums1,nums2):

    merged=[]
    i,j=0,0

    while i<len(nums1) and j<len(nums2):

        if nums1[i]<=nums2[j]:
            merged.append(nums1[i])
            i+=1
        else:
            merged.append(nums2[j])
            j+=1

    etc1=nums1[i:]
    etc2=nums2[j:]

    return merged+etc1+etc2

l=list(range(100))
random.shuffle(l)
print(merging(l))

