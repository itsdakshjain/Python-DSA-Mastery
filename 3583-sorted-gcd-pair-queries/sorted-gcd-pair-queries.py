class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_val = max(nums)
        
        counts = [0] * (max_val + 1)
        for num in nums:
            counts[num] += 1
            
        cnt = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            for j in range(i, max_val + 1, i):
                cnt[i] += counts[j]
                
        f = [0] * (max_val + 1)
        for i in range(max_val, 0, -1):
            total_pairs = cnt[i] * (cnt[i] - 1) // 2
            minus = 0
            for j in range(2 * i, max_val + 1, i):
                minus += f[j]
            f[i] = total_pairs - minus
            
        pref = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            pref[i] = pref[i - 1] + f[i]
            
        ans = []
        for q in queries:
            idx = bisect.bisect_right(pref, q)
            ans.append(idx)
            
        return ans