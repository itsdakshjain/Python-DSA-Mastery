from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = Counter(text)
        
        b_count = counts['b']
        a_count = counts['a']
        l_count = counts['l'] // 2
        o_count = counts['o'] // 2
        n_count = counts['n']
        
        return min(b_count, a_count, l_count, o_count, n_count)