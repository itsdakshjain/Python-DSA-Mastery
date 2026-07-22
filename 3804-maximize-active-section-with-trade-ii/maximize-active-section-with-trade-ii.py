class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        total_ones = s.count('1')
        
        zero_groups = []
        zero_group_idx = [-1] * n
        
        i = 0
        while i < n:
            if s[i] == '0':
                start = i
                while i < n and s[i] == '0':
                    i += 1
                group_id = len(zero_groups)
                zero_groups.append((start, i - start))
                for j in range(start, i):
                    zero_group_idx[j] = group_id
            else:
                i += 1
                
        num_groups = len(zero_groups)
        
        if num_groups < 2:
            return [total_ones] * len(queries)
            
        merged_lengths = [
            zero_groups[k][1] + zero_groups[k + 1][1] 
            for k in range(num_groups - 1)
        ]
        
        m = len(merged_lengths)
        if m > 0:
            k_val = m.bit_length()
            st = [[0] * m for _ in range(k_val)]
            st[0] = list(merged_lengths)
            
            for j in range(1, k_val):
                length = 1 << (j - 1)
                for idx in range(m - (1 << j) + 1):
                    st[j][idx] = max(st[j - 1][idx], st[j - 1][idx + length])
                    
            def query_st(l, r):
                if l > r:
                    return 0
                j = (r - l + 1).bit_length() - 1
                return max(st[j][l], st[j][r - (1 << j) + 1])
        else:
            def query_st(l, r):
                return 0

        next_zero_group = [-1] * (n + 1)
        curr = num_groups
        for idx in range(n - 1, -1, -1):
            if s[idx] == '0':
                curr = zero_group_idx[idx]
            next_zero_group[idx] = curr

        prev_zero_group = [-1] * (n + 1)
        curr = -1
        for idx in range(n):
            if s[idx] == '0':
                curr = zero_group_idx[idx]
            prev_zero_group[idx] = curr
                
        ans = []
        
        for l, r in queries:
            active_sections = total_ones
            
            g_l = zero_group_idx[l]
            g_r = zero_group_idx[r]
            
            first_full = g_l + 1 if g_l != -1 else next_zero_group[l]
            last_full = g_r - 1 if g_r != -1 else prev_zero_group[r]
            
            if first_full <= last_full - 1:
                active_sections = max(active_sections, total_ones + query_st(first_full, last_full - 1))
                
            if s[l] == '0':
                start, length = zero_groups[g_l]
                left_len = length - (l - start)
                if first_full <= last_full:
                    active_sections = max(active_sections, total_ones + left_len + zero_groups[first_full][1])
                    
            if s[r] == '0':
                start, length = zero_groups[g_r]
                right_len = r - start + 1
                if first_full <= last_full:
                    active_sections = max(active_sections, total_ones + right_len + zero_groups[last_full][1])
                    
            if s[l] == '0' and s[r] == '0':
                left_len = zero_groups[g_l][1] - (l - zero_groups[g_l][0])
                right_len = r - zero_groups[g_r][0] + 1
                if g_l + 1 == g_r:
                    active_sections = max(active_sections, total_ones + left_len + right_len)
                
            ans.append(active_sections)
            
        return ans