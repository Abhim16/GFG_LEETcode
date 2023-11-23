class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l,h = 0,n-1
        st,end = -1,-1
        while l<=h:
            mid = (l+h)//2
            if nums[mid] == target:
                st = mid
                h = mid-1
            elif nums[mid]<target:
                l = mid+1
            else:
                h = mid-1
        l,h = 0,n-1
        while l<=h:
            mid = (l+h)//2
            if nums[mid] == target:
                end = mid
                l = mid+1
            elif nums[mid]<target:
                l = mid+1
            else:
                h = mid-1
        return [st,end]        
            
        