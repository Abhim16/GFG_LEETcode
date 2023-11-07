class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max  = float('-inf')
        sum = 0
        for i in range(n):
            sum+=nums[i]
            if max<sum:
                max = sum
            if sum < 0:
                sum = 0
        
            
        return max