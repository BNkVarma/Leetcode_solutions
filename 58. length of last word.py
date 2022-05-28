class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.split() #trims and sets all the words into a list
        return len(s[-1])
        
