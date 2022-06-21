from collections import Counter
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        dict1=Counter(candyType)
        print(dict1)
        result= len(candyType)//2
        
        if result <= len(dict1):
            return result
        if result > len(dict1):
            return len(dict1)
            
        
