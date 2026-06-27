class Solution:
     def maximumLength(self, nums: List[int]) -> int:
        counts = Counter(nums)
        ans = 0
        
        if 1 in counts:
            ans = counts[1] if counts[1] % 2 != 0 else counts[1] - 1
            
        for x in counts:
            if x == 1:
                continue
                
            curr = 0
            while x in counts:
                if counts[x] >= 2:
                    curr += 2
                    x = x * x
                else:
                    curr += 1
                    break
            else:
                curr -= 1
                
            ans = max(ans, curr)
            
        return ans