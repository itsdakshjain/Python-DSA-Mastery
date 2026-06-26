class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        offset = n + 1
        bit = [0] * (2 * n + 2)
        
        def update(idx, val):
            while idx < len(bit):
                bit[idx] += val
                idx += idx & (-idx)
                
        def query(idx):
            s = 0
            while idx > 0:
                s += bit[idx]
                idx -= idx & (-idx)
            return s
            
        ans = 0
        current_pref = 0
        update(current_pref + offset, 1)
        
        for num in nums:
            current_pref += 1 if num == target else -1
            ans += query(current_pref + offset - 1)
            update(current_pref + offset, 1)
            
        return ans