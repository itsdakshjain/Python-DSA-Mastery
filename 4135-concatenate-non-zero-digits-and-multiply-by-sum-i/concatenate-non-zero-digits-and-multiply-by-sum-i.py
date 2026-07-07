class Solution:
    def sumAndMultiply(self, n: int) -> int:
        digits = [c for c in str(n) if c != '0']
        if not digits:
            return 0
        x = int("".join(digits))
        digit_sum = sum(int(c) for c in digits)
        return x * digit_sum
        