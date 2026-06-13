class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result = []
        
        for word in words:
            total_weight = sum(weights[ord(char) - ord('a')] for char in word)
            
            remainder = total_weight % 26
            mapped_char = chr(ord('z') - remainder)
            
            result.append(mapped_char)
            
        return "".join(result)