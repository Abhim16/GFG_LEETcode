from typing import List

class Solution:
    def largestIsland(self, grid : List[List[int]]) -> int:
        
        # Code here
        n=len(grid)
        s=0
        for i in range(n):
            s += sum(grid[i])
        
        if s==n*n:
            return n*n
        
        d={}
        c=2
        t=[0]
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    markisland(grid,i,j,n,c,t)
                    d[c]=t[0]
                    t[0]=0
                    c+=1
        d[0]=0
        ans=1
        for i in range(n):
            for j in range(n):
                if grid[i][j]==0:
                    around=set()
                    if i-1>=0:
                        around.add(grid[i-1][j])
                    if j-1>=0:
                        around.add(grid[i][j-1])
                    if i+1<n:
                        around.add(grid[i+1][j])
                    if j+1<n:
                        around.add(grid[i][j+1])
                    s=1
                    for each in around:
                        s+=d[each]
                    ans=max(ans,s)
        return ans
        
        
def markisland(arr,i,j,n,c,t):
    if arr[i][j]==1:
        arr[i][j]=c
        t[0]+=1
        if i-1>=0:
            markisland(arr,i-1,j,n,c,t)
        if j-1>=0:
            markisland(arr,i,j-1,n,c,t)
        if i+1<n:
            markisland(arr,i+1,j,n,c,t)
        if j+1<n:
            markisland(arr,i,j+1,n,c,t)
    return 
        




#{ 
 # Driver Code Starts

class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        grid=IntMatrix().Input(n,n)
        
        obj = Solution()
        res = obj.largestIsland(grid)
        
        print(res)
# } Driver Code Ends