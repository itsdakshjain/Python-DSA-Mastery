class Solution:
    def smallestPalindrome(self, s: str) -> str:
        half_len = len(s) // 2
        first_half = sorted(s[:half_len])
        
        if len(s) % 2 == 1:
            middle = s[half_len]
            return "".join(first_half) + middle + "".join(reversed(first_half))
        else:
            return "".join(first_half) + "".join(reversed(first_half))