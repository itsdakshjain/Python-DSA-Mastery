class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1
        
        if n == 1:
            return m
        
        dp_up = [v for v in range(m)]
        dp_down = [(m - 1 - v) for v in range(m)]
        
        if n == 2:
            return (sum(dp_up) + sum(dp_down)) % MOD
        
        X = dp_up + dp_down
        size = 2 * m
        
        T = [[0] * size for _ in range(size)]
        
        for v in range(m):
            for u in range(v):
                T[v][m + u] = 1
            for u in range(v + 1, m):
                T[m + v][u] = 1

        def multiply(A, B):
            C = [[0] * size for _ in range(size)]
            for i in range(size):
                for k in range(size):
                    if not A[i][k]:
                        continue
                    for j in range(size):
                        C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
            return C

        def power(A, p):
            res = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
            base = A
            while p > 0:
                if p % 2 == 1:
                    res = multiply(res, base)
                base = multiply(base, base)
                p //= 2
            return res

        T_pow = power(T, n - 2)
        
        ans = 0
        for i in range(size):
            row_sum = 0
            for j in range(size):
                row_sum = (row_sum + T_pow[i][j] * X[j]) % MOD
            ans = (ans + row_sum) % MOD
            
        return ans