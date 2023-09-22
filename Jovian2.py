#Merge sort

import random

def msort(nums):

    if len(nums)<=1:
        return nums
    
    mid=len(nums)//2

    left=nums[:mid]
    right=nums[mid:]

    lefts= msort(left)
    rights=msort(right)

    msorted= merge(lefts, rights)

    return msorted

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

    extra1=nums1[i:]
    extra2=nums2[j:]

    return merged+extra1+extra2

l=list(range(100000))
random.shuffle(l)
print(msort(l))
    