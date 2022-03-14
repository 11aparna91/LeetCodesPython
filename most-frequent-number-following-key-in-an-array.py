### Problem Number: 2190
from typing import List
class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        
        def get_key(max_val: int) -> int:
            for i,val in dict1.items():
                if val==max_val:
                    return i      
        count=0
        index=[]
        for i in range(len(nums)):
            if nums[i] == key:
                index.append(i)
        dict1={}
        for k in index:
            if k==len(nums) or k==len(nums)-1:
                break
            elif nums[k+1] not in dict1:
                dict1[nums[k+1]]=1
            else:
                dict1[nums[k+1]] +=1
        print(dict1)
        
        max_val= max(dict1.values())
        return get_key(max_val)
       
