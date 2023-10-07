#User function Template for python3

class Solution:
    def minRow(self,N,M,A):
        #code here
        
        
        min = float('inf')
        min_row = -1
        for i in range(N):
            count = 0
            for j in range(M):
                if A[i][j] == 1:
                    count+=1
            if min>count:
                min = count
                min_row  = i
            
        if min_row == -1:
            return 1
        return min_row+1       
                
            
                
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split(" "))
        A=[]
        for i in range(N):
            B=list(map(int,input().strip().split(" ")))
            A.append(B)
        ob=Solution()
        print(ob.minRow(N,M,A))
# } Driver Code Ends