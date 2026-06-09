class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        max_val = max(nums)
        min_val = min(nums)

        return k * (max_val - min_val)