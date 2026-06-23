class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1
        
        if m <= 0:
            return 0
        
        dp0 = [1] * m
        dp1 = [1] * m
        
        for _ in range(1, n):
            new_dp0 = [0] * m
            new_dp1 = [0] * m
            
            p1 = 0
            for j in range(m):
                new_dp0[j] = p1 % MOD
                p1 += dp1[j]
                
            p0 = 0
            for j in range(m - 1, -1, -1):
                new_dp1[j] = p0 % MOD
                p0 += dp0[j]
                
            dp0 = new_dp0
            dp1 = new_dp1
            
        return (sum(dp0) + sum(dp1)) % MOD