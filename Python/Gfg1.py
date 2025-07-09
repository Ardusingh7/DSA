l=[2,5,3]

s1=0
s2=0

for i in range(len(l)):
    if i%2==0:
        s1+=l[i]
    else:
        s2+=l[i]

if(s2>=s1):
    print(s2)
else:
    print(s1)