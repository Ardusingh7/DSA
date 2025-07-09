def largeOdd(n):

    while len(n)>0:
        if int(n[-1])%2!=0:
            return n
        else:
            n=n[:len(n)-1]

print(largeOdd("124689"))