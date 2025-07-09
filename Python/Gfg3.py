#User function Template for python3
class Solution:
    def minTime(self, N, X, src, dest, M1, M2, airlines, railways):
        #code here
        
            l=[]
            l2=[]
            
            if M1==1:
                if (airlines[0]==src and airlines[1]==dest):
                    l.append(airlines[2])
                else:
                    for j in range(M1):
                        if (airlines[j][0]==src and airlines[j][1]==dest):
                            l.append(airlines[j][2])
                            
            if M2==1:
                if (railways[0]==src and railways[1]==dest):
                    l2.append(railways[2])
                else:
                    for j in range(M2):
                        if ((railways[j][0])==src and (railways[j][1])==dest):
                            l2.append(railways[j][2])
                            
            if l2!=[]:
                return min(l2)
            else:
                return -1
                    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N,X = map(int,input().strip().split())
        src,dest = map(int,input().strip().split())
        
        M1 = int(input())
        airlines = []
        for i in range(M1):
            e = list(map(int, input().strip().split()))
            airlines.append(e)
        M2 = int(input())
        railways = []
        for i in range(M2):
            e = list(map(int, input().strip().split()))
            railways.append(e)
            
        ob = Solution()
        ans = ob.minTime(N, X, src, dest, M1, M2, airlines, railways)
        print(ans)
# } Driver Code Ends