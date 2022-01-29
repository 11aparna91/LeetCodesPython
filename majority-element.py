class Solution:
     def majorityElement(self, nums: List[int]) -> int:
        def get_key(val):
            for key, value in dict1.items():
                if val == value:
                     return key
   
        dict1={}
        for i in nums:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
        maxi=max(dict1.values())
        return get_key(maxi)
        
########################Another Solution###############################

class Solution:
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)
      
####################################3rd Solution#######################################

class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]
