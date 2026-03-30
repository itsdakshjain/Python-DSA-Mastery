class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        # Step 1: Separate characters into even and odd positions
        s1_even = sorted(s1[0::2])
        s1_odd = sorted(s1[1::2])
        
        s2_even = sorted(s2[0::2])
        s2_odd = sorted(s2[1::2])
        
        # Step 2: Compare the sorted groups
        return s1_even == s2_even and s1_odd == s2_odd