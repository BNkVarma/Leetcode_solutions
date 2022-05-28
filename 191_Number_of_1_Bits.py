class Solution:
    def hammingWeight(self, n:int)->int:
        rem=0
        while n>0:
            rem+=n%2
            n=n//2
        return rem
