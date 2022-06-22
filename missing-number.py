#### Time Complexity=O(n) Space Complexity=O(n) ############

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        size=len(nums)
        mod_arr=[]
        for i in range(1,size+1):
            mod_arr.append(i)
            
        diff=sum(mod_arr) - sum(nums)
        return diff
            
        
