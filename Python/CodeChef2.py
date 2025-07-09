# cook your dish here
n=int(input())

for i in range(n):

    for j in range(1):
        l=list(map(int,(input().split())))
      
    x=l[0]
    
    l2=[]
    for k in range(x):
        l2.append(int(input()))
    
    s=0
    for m in l2:

      if l[1]>0:
          l[1]=l[1]-m
    print(l[1])
      
    

    