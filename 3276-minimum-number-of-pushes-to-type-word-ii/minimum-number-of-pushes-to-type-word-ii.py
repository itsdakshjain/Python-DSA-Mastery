class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word)
        sorted_freqs = sorted(freq.values(), reverse=True)
        
        total_pushes = 0
        for i, count in enumerate(sorted_freqs):
            pushes_per_press = (i // 8) + 1
            total_pushes += count * pushes_per_press
            
        return total_pushes