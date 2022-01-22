class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        nums2=[]
        for i in range(len(nums)):
            nums2.append(nums[nums[i]])
        return nums2
      
#######Another Solution with the space complexity as O(1)#################

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for i in range(n):
            nums[i] = nums[i] + (n* (nums[nums[i]]%n))
    
        for i in range(n):
            nums[i] =nums[i]//n
            
        return nums
        
        
        
