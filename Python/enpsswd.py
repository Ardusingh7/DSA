def check(e,k):

    s=''
    for i in e:
        s += chr((ord(i) - ord('a') + k) % 26 + ord('a'))

    return s

print(check('zyx',1))