
class Solution:
    import bisect
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        
        return bisect.bisect(nums,target)
