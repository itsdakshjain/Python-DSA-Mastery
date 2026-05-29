class Solution:
    def minElement(self, nums: List[int]) -> int:
        min_sum = float('inf')
        
        for num in nums:
            digit_sum = 0
            temp = num
            
            while temp > 0:
                digit_sum += temp % 10
                temp //= 10
                
            if digit_sum < min_sum:
                min_sum = digit_sum
                
        return min_sum