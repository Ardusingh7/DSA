def char_frequency(str1):
    d = {}
    keys = d.keys()
    for n in str1:
        if n in keys:
            
            d[n] += 1
        else:
            d[n] = 1
            
    d2 = sorted(d.items())
    return d2

print(char_frequency('cdef abcd efgh abcd efgh @@ ## $$'))

