def gbset(x):

    for i in range(len(x)):
        for j in range(i+1,len(x)):
            
            if x[i] in x[j]:
                return('BAD SET', x[j])
            
    return "GOOD SET"

print(gbset(['aab',
'aac',
'aacghgh',
'aabghgh']))