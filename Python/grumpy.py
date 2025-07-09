# Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3
# Output: 16

customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]

total= 0

for i in range(len(customers)):

    if grumpy[i]==0:
        total+= customers[i]
    
#print(total)

l=0
r=0

mins= 3

maxTotal=0

while r<=len(customers)-mins:

    s=total

    for i in range(l, r+mins):
        if grumpy[i]==1:
            s+= customers[i]
            #print(total, s)
    maxTotal= max(s, total) 
    l+=1
    r+=1

print(maxTotal)