#####################################Problem Number 448#####################################
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums=list(set(range(1,len(nums)+1)) - set(nums))
        return nums
 

########################Another Solution #####################################################


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hash_table = {}
        
        # Add each of the numbers to the hash table
        for num in nums:
            hash_table[num] = 1
        
        # Response array that would contain the missing numbers
        result = []    
        
        # Iterate over the numbers from 1 to N and add all those
        # that don't appear in the hash table. 
        for num in range(1, len(nums) + 1):
            if num not in hash_table:
                result.append(num)
                
        return result  
################ Time Complexity O(N) and space complexity O(N)
