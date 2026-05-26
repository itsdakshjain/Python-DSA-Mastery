class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        unique_chars = set(word)
        count = 0
        
        for i in range(26):
            lower = chr(ord('a') + i)
            upper = chr(ord('A') + i)
            if lower in unique_chars and upper in unique_chars:
                count += 1
                
        return count # for leatsync