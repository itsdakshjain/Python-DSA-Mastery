class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def count_waviness(n: int) -> int:
            if n < 100:
                return 0
            
            s = str(n)
            length = len(s)
            
            import functools
            @functools.lru_cache(None)
            def dp(idx, last1, last2, is_less, is_started):
                if idx == length:
                    return 0
                
                limit = 9 if is_less else int(s[idx])
                ans = 0
                
                for d in range(limit + 1):
                    next_is_less = is_less or (d < limit)
                    
                    if not is_started:
                        if d == 0:
                            ans += dp(idx + 1, -1, -1, next_is_less, False)
                        else:
                            ans += dp(idx + 1, d, -1, next_is_less, True)
                    else:
                        waviness = 0
                        if last2 != -1:
                            if last1 > last2 and last1 > d:
                                waviness = 1
                            elif last1 < last2 and last1 < d:
                                waviness = 1
                        
                        ways = dp_ways(idx + 1, d, last1, next_is_less)
                        ans += waviness * ways + dp(idx + 1, d, last1, next_is_less, True)
                        
                return ans

            @functools.lru_cache(None)
            def dp_ways(idx, last1, last2, is_less):
                if idx == length:
                    return 1
                
                limit = 9 if is_less else int(s[idx])
                ans = 0
                
                for d in range(limit + 1):
                    next_is_less = is_less or (d < limit)
                    ans += dp_ways(idx + 1, d, last1, next_is_less)
                    
                return ans

            return dp(0, -1, -1, False, False)

        return count_waviness(num2) - count_waviness(num1 - 1)