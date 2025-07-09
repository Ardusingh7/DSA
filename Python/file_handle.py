f=open('C:/Users/adusi/Downloads/Graffiti.txt','r+')
a=f.readlines()
cnt1=0
cnt2=0
cnt3=0
for i in a:
    cnt1+=1
    for j in i:
        cnt2+=1
f.seek(0)
for i in f.read():
    print(i)
    cnt3+=1
print(cnt1,cnt2,cnt3)
