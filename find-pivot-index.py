## Time Complexity=O(n) #########
## Space Complexity=O(1) ########
#### Problem Number 724 #########
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        leftSum=0
        
        totalSum=sum(nums)
        for i,x in enumerate(nums):
            if leftSum == (totalSum - leftSum - x):
                return i
            leftSum +=x
                
        return -1
            
   
