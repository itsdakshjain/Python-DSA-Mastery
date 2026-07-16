class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        prefixGcd = []
        mx = 0
        for x in nums:
            if x > mx:
                mx = x
            prefixGcd.append(math.gcd(x, mx))
        
        prefixGcd.sort()
        
        total_sum = 0
        left = 0
        right = n - 1
        
        while left < right:
            total_sum += math.gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1
            
        return total_sum