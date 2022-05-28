class Solution:
    def reverse(self, x: int) -> int:
        
        if x>=0:
            s=str(x)
        else:
            s=str(abs(x))
            s+='-'
        num=int(s[::-1])
        if -2**31<=num<=(2**31)-1: 
            return num
        return 0
        
