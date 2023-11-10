class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        mid,l,h = 0,0,n-1
        while(mid<=h):
            if nums[mid] == 0:
                nums[l],nums[mid] = nums[mid],nums[l]
                l+=1
                mid+=1
            elif nums[mid] == 1:
                mid+=1
            elif nums[mid] == 2:
                nums[mid],nums[h] = nums[h],nums[mid]
                h-=1
        return nums        
                
        