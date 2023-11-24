class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        l,h = 0,n-1
        while(l<=h):
            mid = (l+h)//2
            if nums[mid] == target:
                return True
            if nums[l] == nums[mid] and nums[l] == nums[h]:
                l+=1
                h-=1
                continue
            if nums[l]<=nums[mid]:
                if nums[l]<=target and target<=nums[mid]:
                    h = mid-1
                else:
                    l = mid+1
            else:
                if nums[mid]<=target and target<=nums[h]:
                    l = mid+1
                else:
                    h = mid-1
        return False           
                    
        