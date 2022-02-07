#################### Problem number: 217 ##########################


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict2={}
        
        for i in nums:
            if i not in dict2:
                dict2[i]=1
            else:
                dict2[i]+=1
                return True
        
        return False
      
##############################################
