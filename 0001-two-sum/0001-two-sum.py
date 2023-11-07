class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number = list(enumerate(nums))
        number.sort(key = lambda x:x[1])
        left,right = 0,len(nums)-1
        while(left<right):
            cur_sum = number[left][1]+number[right][1]
            if cur_sum == target:
                return [number[left][0],number[right][0]]
            elif cur_sum > target:
                right-=1
            else:
                left+=1
                
        
#         nums_with_indices = list(enumerate(nums))  # Create a list of tuples (index, value)
        # nums_with_indices.sort(key=lambda x: x[1])  # Sort the list of tuples based on values

#         left, right = 0, len(nums) - 1

#         while left < right:
#             current_sum = nums_with_indices[left][1] + nums_with_indices[right][1]
#             if current_sum == target:
#                 return [nums_with_indices[left][0], nums_with_indices[right][0]]
#             elif current_sum < target:
#                 left += 1
#             else:
#                 right -= 1

#         return []        
            
        