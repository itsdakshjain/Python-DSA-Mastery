class Solution:
    def countFactors (self, n):
        count=1#checking extension
        for i in range(1,(n//2) +1):
            if n%i==0:
                count=count+1
        return count     
                