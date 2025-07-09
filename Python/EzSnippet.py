def log_check(num,l):
    
    s=0
    cnt=0

    for i in sorted(l):
        s+=i
        cnt+=1
        if s>=num:
            break
    
    if s==num:
        return cnt
    elif s>num:
        if (s-num) in l:
            return cnt-1
    
    return "Not possible"

print(log_check(15,[1,2,4,6,8,10]))