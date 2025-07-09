s = "Bawds jog, flick quartz, vex nymph"
x=set(s)
cnt=0

for i in x:
    if i=="" or i==',':
        continue
    else:
        cnt+=1

print(cnt)
