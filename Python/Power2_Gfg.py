import math

def check(n):
        
        x=math.log(n)
        y=math.log(2) 
        
        if 2**(x/y)==n:
            return "Yes"
        else:
            return "No"
        
print(check(3))