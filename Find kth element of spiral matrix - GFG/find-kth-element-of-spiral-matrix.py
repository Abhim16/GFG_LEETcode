#User function Template for python3

class Solution:
    def findK(self, a, n, m, k):
        # Write Your Code here
        row,col = 0,0
        # r == matrix.lenght
        # c == matrix[i].lenght
        m = len(a)
        n = len(a[0])
        res = []
        while (row<m and col < n ):
            for i in range(col,n):
                res.append(a[row][i])
            row+=1
            for i in range(row,m):
                res.append(a[i][n-1])
            n-=1
            if (row<m):
                for i in range(n-1,col-1,-1):
                    res.append(a[m-1][i])
                m-=1
            if (col<n):
                for i in range(m-1,row-1,-1):
                    res.append(a[i][col])
                col+=1
        return res[k-1]         


#{ 
 # Driver Code Starts

#Initial Template for Python 3

for _ in range(int(input())):
    n, m, k = map(int,input().split())
    a = [
            list(map(int,input().split()))
            for _ in range(n)
        ]
    
    ob = Solution()
    print(ob.findK(a,n,m,k))
    
# } Driver Code Ends