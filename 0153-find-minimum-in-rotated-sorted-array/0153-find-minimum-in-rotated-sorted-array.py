class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l,h = 0,n-1
        minn = nums[0]
        while l<=h:
            mid = (l+h)//2
            if nums[l]<=nums[mid]:
                minn = min(minn,nums[l])
                l = mid+1
            else:
                minn = min(minn,nums[mid])
                h = mid-1
        return minn        
            