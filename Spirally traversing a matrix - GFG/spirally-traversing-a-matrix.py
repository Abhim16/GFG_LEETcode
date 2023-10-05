#User function Template for python3

class Solution:
    
    #Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self,matrix, r, c): 
        # code here 
        row,col = 0,0
        res = []
        while (row<r and col<c):
            for i in range(col,c):
                res.append(matrix[row][i])
            row+=1
            for i in range(row,r):
                res.append(matrix[i][c-1])
            c-=1
            if (row<r):
                for i in range(c-1,col-1,-1):
                    res.append(matrix[r-1][i])
                r-=1
            if (col<c):
                for i in range(r-1,row-1,-1):
                    res.append(matrix[i][col])
                col+=1
        return res            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(r):
            row=[]
            for j in range(c):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.spirallyTraverse(matrix,r,c)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends