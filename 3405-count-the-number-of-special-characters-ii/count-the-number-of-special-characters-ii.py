class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        last_lower = [-1] * 26
        first_upper = [-1] * 26
        
        for idx, char in enumerate(word):
            if char.islower():
                last_lower[ord(char) - ord('a')] = idx
            else:
                ascii_idx = ord(char) - ord('A')
                if first_upper[ascii_idx] == -1:
                    first_upper[ascii_idx] = idx
                    
        special_count = 0
        for i in range(26):
            if last_lower[i] != -1 and first_upper[i] != -1:
                if last_lower[i] < first_upper[i]:
                    special_count += 1
                    
        return special_count