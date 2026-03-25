class Solution:
    def reverse(self, x: int) -> int:
        is_negative = False
        if x<0:
            is_negative = True
        num=abs(x)
        reverse=0
        while num>0 :
            last_digit = num%10
            reverse = last_digit + (reverse*10)
            num = num//10
        
        if reverse < (-(21**31)) or reverse > (2**31 - 1):
            return 0
        return -reverse if is_negative else reverse
