s="1ab12abc123"
l=[]

st=""

for i in s:
    if i.isnumeric():
        st=st+i
    else:
        l.append(st)
        st=""
l.append(st)

s=0

for i in l:
    if i.isnumeric():
        s+=int(i)

print(s)