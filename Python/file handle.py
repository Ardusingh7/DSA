f=open('num.txt','r+')
f2=open('odd.txt','w+')
f3=open('even.txt','w+')

n=f.read()
m=n.split(' ')
for i in m:
    if int(i)%2==0:
        f3.write(i)
    else:
        f2.write(i)

f.close()
f2.close()
f3.close()

print('done')
