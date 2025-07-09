def solve(n,cap):

    if n==0 or cap==0:
        return False
    else:

        cwt=wt[n-1]
        cv=val[n-1]

        if cwt<=cap:

            c1=cv+solve(n-1,cap-cwt)
            c2=solve(n-1,cap)

            return max(c1,c2)
        
        else:
            return solve(n-1,cap)
        
    return solve(N,W)

