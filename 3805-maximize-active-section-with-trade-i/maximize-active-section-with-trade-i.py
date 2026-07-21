class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        t = "1" + s + "1"
        
        ones = []
        zeros = []
        
        i = 0
        n = len(t)
        while i < n:
            j = i
            while j < n and t[j] == t[i]:
                j += 1
            length = j - i
            if t[i] == '1':
                ones.append(length)
            else:
                zeros.append(length)
            i = j
            
        initial_ones = s.count('1')
        
        if len(ones) <= 2:
            return initial_ones
            
        max_gain = 0
        
        for i in range(1, len(ones) - 1):
            gain1 = zeros[i - 1] + zeros[i]
            max_gain = max(max_gain, gain1)
            
        max_z1, max_z2 = -1, -1
        idx1, idx2 = -1, -1
        
        for idx, z in enumerate(zeros):
            if z > max_z1:
                max_z2, idx2 = max_z1, idx1
                max_z1, idx1 = z, idx
            elif z > max_z2:
                max_z2, idx2 = z, idx
                
        for i in range(1, len(ones) - 1):
            b_len = ones[i]
            best_z = 0
            if idx1 != i - 1 and idx1 != i:
                best_z = max_z1
            elif idx2 != -1 and idx2 != i - 1 and idx2 != i:
                best_z = max_z2
                
            if best_z > 0:
                max_gain = max(max_gain, best_z - b_len)
                
        return initial_ones + max_gain