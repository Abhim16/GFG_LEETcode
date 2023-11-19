from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
#         count = 0

#         for i in range(n):
#             summ = 0
#             for j in range(i, n):
#                 summ += nums[j]
#                 if summ == k:
#                     count += 1

#         return count
            
        d = {0:1}
        count = 0
        summ = 0
        for i in range(n):
            summ+=nums[i]
            if summ-k in d:
                count+=d[summ-k]
            if summ in d:
                d[summ]+=1
            else:
                d[summ] = 1
        return count  

                