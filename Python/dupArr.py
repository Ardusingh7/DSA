arr=[2,3,1,2,3]

d={}
    	
for i in arr:
    if i in d:
        d[i]+=1
    else:
    	d[i]=1
    	       
l=[]

for i,j in d.items():
    if j>1:
        print(i,end=" ")
        