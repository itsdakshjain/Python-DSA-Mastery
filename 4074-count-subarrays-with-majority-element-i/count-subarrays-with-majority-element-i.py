class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0
        
        for i in range(n):
            current_balance = 0
            for j in range(i, n):
                if nums[j] == target:
                    current_balance += 1
                else:
                    current_balance -= 1
                
                if current_balance > 0:
                    ans += 1
                    
        return ans