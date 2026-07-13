class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        sample = "123456789"
        
        for length in range(len(str(low)), len(str(high)) + 1):
            for start in range(10 - length):
                num = int(sample[start:start + length])
                if low <= num <= high:
                    res.append(num)
                    
        return res