class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        
        A = []
        pos = [0] * (len(s) + 1)
        for i, ch in enumerate(s):
            pos[i + 1] = pos[i]
            if ch != '0':
                A.append(int(ch))
                pos[i + 1] += 1
                
        n = len(A)
        P = [0] * (n + 1)
        S = [0] * (n + 1)
        for i in range(n):
            P[i + 1] = (P[i] * 10 + A[i]) % MOD
            S[i + 1] = S[i] + A[i]
            
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD
            
        ans = []
        for l, r in queries:
            L = pos[l]
            R = pos[r + 1] - 1
            if L > R:
                ans.append(0)
            else:
                x = (P[R + 1] - P[L] * pow10[R - L + 1]) % MOD
                total_sum = S[R + 1] - S[L]
                ans.append((x * total_sum) % MOD)
                
        return ans