class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        if n == 0:
            return []
            
        U = sorted(list(set(nums)))
        m = len(U)
        val_to_idx = {val: i for i, val in enumerate(U)}
        
        LOG = 18
        up = [[0] * m for _ in range(LOG)]
        
        for i in range(m):
            target = U[i] + maxDiff
            idx = bisect.bisect_right(U, target) - 1
            up[0][i] = idx
            
        for k in range(1, LOG):
            for i in range(m):
                up[k][i] = up[k-1][up[k-1][i]]
                
        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
                continue
                
            valA, valB = nums[u], nums[v]
            if valA == valB:
                ans.append(1)
                continue
                
            idxA, idxB = val_to_idx[valA], val_to_idx[valB]
            if idxA > idxB:
                idxA, idxB = idxB, idxA
                
            if up[LOG-1][idxA] < idxB:
                ans.append(-1)
                continue
                
            steps = 0
            curr = idxA
            for k in range(LOG - 1, -1, -1):
                if up[k][curr] < idxB:
                    steps += (1 << k)
                    curr = up[k][curr]
            
            ans.append(steps + 1)
            
        return ans