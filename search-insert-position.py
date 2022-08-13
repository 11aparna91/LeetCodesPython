############### Problem Number 35 ###############
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)

########## Time complexity=O(log n) ############
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        
        while l<=r:
            mid=(l+r)//2
            if nums[mid] == target:
                return mid
            else:
                if nums[mid]<target:
                    l=mid+1
                else:
                    r=mid-1
        return l
