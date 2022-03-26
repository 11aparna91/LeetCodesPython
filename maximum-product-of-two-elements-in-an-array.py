#Complexity for the heapq is log(n)
import heapq
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        arr=[]
        arr=heapq.nlargest(2,nums)
        
        result=1
        for i in arr:
            result = result * (i-1)
        return result
  
  
###### Second Solution #######
import heapq
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        arr=heapq.nlargest(2,nums)
        return (arr[0]-1) * (arr[1]-1)
      
      
############################################ 3rd Solution #########

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        first=second=0
        for n in nums:
            if n>first:
                second=first
                first=n      
            else:
                second=max(second,n)
        return (first-1) * (second-1)

                
            
            
            
        
