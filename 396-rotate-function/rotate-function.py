class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        f = sum(i * num for i, num in enumerate(nums))
        ans = f

        for i in range(n - 1, 0, -1):
            f = f + total_sum - n * nums[i]
            if f > ans:
                ans = f
                
        return ans