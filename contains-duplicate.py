#################### Problem number: 217 ##########################

################## Using Hash Table ###############################
############# Time Complexity=O(n) ################################
################# Space Complexity=O(n) ###########################
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
      
############################################## Solution 2#############
######################################## Using Sorting ###############
########################### Time Complexity=O(nlogn) (WORST CASE COMPLEXITY OF SORTING)########
########################### Space Complexity=O(1) ####################
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False
