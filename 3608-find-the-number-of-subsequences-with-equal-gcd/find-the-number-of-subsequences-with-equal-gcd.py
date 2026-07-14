class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        max_val = 200
        MOD = 10**9 + 7
        
        dp = {}
        dp[(0, 0)] = 1
        
        for x in nums:
            next_dp = dp.copy()
            for (g1, g2), count in dp.items():
                ng1 = x if g1 == 0 else math.gcd(g1, x)
                next_dp[(ng1, g2)] = (next_dp.get((ng1, g2), 0) + count) % MOD
                
                ng2 = x if g2 == 0 else math.gcd(g2, x)
                next_dp[(g1, ng2)] = (next_dp.get((g1, ng2), 0) + count) % MOD
            dp = next_dp
            
        ans = 0
        for g in range(1, max_val + 1):
            if (g, g) in dp:
                ans = (ans + dp[(g, g)]) % MOD
                
        return ans