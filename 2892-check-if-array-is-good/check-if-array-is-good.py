class Solution:
    def isGood(self, nums: List[int]) -> bool:

        n = len(nums) - 1
        
        if n < 1:
            return False
        
        nums.sort()
        
        for i in range(n - 1):
            if nums[i] != i + 1:
                return False
        
        return nums[n-1] == n and nums[n] == n