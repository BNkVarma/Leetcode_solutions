class Solution:
    def isValid(self, s: str) -> bool:
        brackets={'(':')','{':'}','[':']'}
        list=[]
        if len(s)%2!=0:
            return False
        for c in s:
            if list and list[-1]==c:
                list.pop()
            else:
                try:
                    list.append(brackets[c])
                except:
                    return False
                    
        return not list
