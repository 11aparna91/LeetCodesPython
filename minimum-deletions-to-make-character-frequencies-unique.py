########### Problem Number 1647 ##############################
########### Time Complexity= O(n) Space Complexity=O(n) ######
class Solution:
    def minDeletions(self, s: str) -> int:
        dict1= collections.Counter(s)
        
        set1=set()
        count=0
        for key,val in dict1.items():
            while val>0 and val in set1:
                val -=1
                count +=1
            set1.add(val)
        return count    
        
