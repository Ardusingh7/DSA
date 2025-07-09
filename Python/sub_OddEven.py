def is_vowel(char):

    return char.lower() in 'aeiou'

def vowel_substrings(s):

    vowel_subs = []
    n = len(s)
    i = 0

    while i < n:
        if is_vowel(s[i]):
            start = i
            while i < n and is_vowel(s[i]):
                i += 1
            vowel_subs.append(s[start:i])
        else:
            i += 1
    
    return vowel_subs

def toCheck(x):

    output=[]

    for i in x:
        y=vowel_substrings(i)
      
        for j in y:  
            odd=[]
            even=[]
            
            if len(j)%2==0:
                even.append(j)
            else:
                odd.append(j)
            
            #print(odd,even) 

        if len(odd)==0:
            output.append("Chris")
        elif len(odd)>len(even):
            output.append("Alex")
        else:
            output.append("Alex")
        
        odd=[]
        even=[]

    print(output)

toCheck(["ljis","thr","gms"])
