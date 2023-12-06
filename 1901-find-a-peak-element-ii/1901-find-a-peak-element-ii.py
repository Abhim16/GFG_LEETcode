# class Solution:
#     def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
#         n = len(mat)
#         m = len(mat[0])
#         ans = []
#         for i in range(n):
#             for j in range(m):
#                 if mat[i][j]>mat[i-1][j] and mat[i][j]>mat[i][j-1]:
#                     ans.append(i)
#                     ans.append(j)
#             break
#         return ans      
from typing import List

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])

        for i in range(n):
            for j in range(m):
                is_peak = True

                if i > 0 and mat[i][j] <= mat[i - 1][j]:
                    is_peak = False
                if i < n - 1 and mat[i][j] <= mat[i + 1][j]:
                    is_peak = False
                if j > 0 and mat[i][j] <= mat[i][j - 1]:
                    is_peak = False
                if j < m - 1 and mat[i][j] <= mat[i][j + 1]:
                    is_peak = False

                if is_peak:
                    return [i, j]

        return []

                
        