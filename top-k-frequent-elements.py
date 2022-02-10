##################################### Problem Number 347 ###################################
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count=Counter(nums)
      
        
        return heapq.nlargest(k,count,key=count.get)
  
 #######################################################################Solution 2 ##################

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count=Counter(nums)
      
        
        return heapq.nlargest(k,count.keys(),key=count.get)
