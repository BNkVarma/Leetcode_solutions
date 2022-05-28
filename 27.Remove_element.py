#Leetcode Remove Element problem, Easy
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        c=0
        while c<len(nums):
            if nums[i]==val:
                temp=nums.pop(i)
                nums.append(temp)
            else:
                i+=1
            c+=1
        return i