class Solution:xxxxxxxxxxxx
    def isPalindrome(self, x: int) -> bool:
        num = x
        reverse = 0
        while num >0:
            last_digit = num % 10
            reverse = last_digit + (reverse*10)
            num = num // 10
        return reverse == x
