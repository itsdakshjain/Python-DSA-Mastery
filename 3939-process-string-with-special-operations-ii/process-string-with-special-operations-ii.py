class Solution:
    def processStr(self, s: str, k: int) -> str:
        lengths = []
        curr_len = 0
        
        for char in s:
            if char.isalpha():
                curr_len += 1
            elif char == '*':
                if curr_len > 0:
                    curr_len -= 1
            elif char == '#':
                curr_len *= 2
            elif char == '%':
                pass
            
            lengths.append(curr_len)
            
        if k >= curr_len or k < 0:
            return '.'
            
        for i in range(len(s) - 1, -1, -1):
            char = s[i]
            prev_len = lengths[i-1] if i > 0 else 0
            
            if char.isalpha():
                if k == curr_len - 1:
                    return char
                curr_len = prev_len
            elif char == '*':
                curr_len = prev_len
            elif char == '#':
                curr_len = prev_len
                if k >= curr_len:
                    k %= curr_len
            elif char == '%':
                curr_len = prev_len
                k = curr_len - 1 - k

        return '.'