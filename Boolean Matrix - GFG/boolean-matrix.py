#User function Template for python3


#Function to modify the matrix such that if a matrix cell matrix[i][j]
#is 1 then all the cells in its ith row and jth column will become 1.
def booleanMatrix(matrix):
    # r = len(matrix)
    # c = len(matrix[0])
    # row,col = 0,0
    # while(row<r-1 and col < c-1):
    #     for i in range(col,c-1):
    #         if matrix[row][i] == 1:
    #             for i in range(col,c-1):
    #                 matrix[row][i] = 1
    #     row+=1            
    #     for i in range(row,r-1):
    #         if matrix[i][col]==1:
    #             for i in range(row,r-1):
    #                 matrix[i][col] = 1
    #     c-=1            
    #     if (row<r-1):
    #         for i in range(c-1,col):
    #             if matrix[r-1][i] == 1:
    #                 for i in range(c-1,col):
    #                     matrix[r-1][i] = 1
    #         r-=1                
    #     if (col<c-1):
    #         for i in range(r-1,row):
    #             if matrix[i][col] == 1:
    #                 for i in range(r-1,row):
    #                     matrix[i][col] = 1
    # return matrix 
    row,col = {},{}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                row[i] = 1
                col[j] = 1
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i in row or j in col:
                matrix[i][j] = 1
    return matrix            
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        matrix = []
        for i in range(r):
            line = [int(x) for x in input().strip().split()]
            matrix.append(line)
        booleanMatrix(matrix)
        for i in range(r):
            for j in range(c):
                print(matrix[i][j], end=' ')
            print()


# } Driver Code Ends