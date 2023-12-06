# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         n = len(matrix)
#         m = len(matrix[0])
#         for i in range(n):
#             for j in range(m):
#                 if i == j:
#                     if matrix[i][j]<target:
#                         continue
#                     for k in range(n):
#                         if matrix[k][j] == target:
#                             return True
#                     for k in range(m):
#                         if matrix[i][k] == target:
#                             return True
#         return False                  
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        
        for i in range(n):
            if matrix[i][m - 1] < target:
                continue

            l, h = 0, m - 1
            while l <= h:
                mid = (l + h) // 2
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] > target:
                    h = mid - 1
                else:
                    l = mid + 1

        return False
                        
        