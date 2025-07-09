a='aa bb aa bb aa bb aa bb'
b=a.split(' ')
c=input()
cnt=0
for i in b:
    if i[0]==c:
        cnt+=1
print(cnt)
