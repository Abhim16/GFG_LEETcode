class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead."""
        n = len(nums)
        k = k%n
        arr = []
        for i in range(n-k,n):
            arr.append(nums[i])
        for i in range(n-k):
            arr.append(nums[i])
        for i in range(n):
            nums[i] = arr[i]
           
        