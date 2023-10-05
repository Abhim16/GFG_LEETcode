class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row,col = 0,0
        # r == matrix.lenght
        # c == matrix[i].lenght
        m = len(matrix)
        n = len(matrix[0])
        res = []
        while (row<m and col < n ):
            for i in range(col,n):
                res.append(matrix[row][i])
            row+=1
            for i in range(row,m):
                res.append(matrix[i][n-1])
            n-=1
            if (row<m):
                for i in range(n-1,col-1,-1):
                    res.append(matrix[m-1][i])
                m-=1
            if (col<n):
                for i in range(m-1,row-1,-1):
                    res.append(matrix[i][col])
                col+=1
        return res        
        
        