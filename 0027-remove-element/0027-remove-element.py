class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
#         for i in nums:
#             if i == val:
#                 nums.remove(i)
                
#         print(nums)    
        nums[:] = [x for x in nums if x!=val]
        return(len(nums))
    
        # nums.remove(" ")
        # print(nums)
        # for i in range(len(nums)):
        #     if nums[i] == val:
        #         nums.remove(i)
        # return len(nums)+1        
        # nums.remove(val)
        # return len(nums)+1    
        