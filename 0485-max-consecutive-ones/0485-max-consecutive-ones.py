class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        summ = 0
        maxi = 0
        for i in range(n):
            if nums[i] == 1:
                summ+=nums[i]
                maxi = max(maxi,summ)
            else:
                summ = 0
        return maxi       
            
        