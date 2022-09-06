from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict1=Counter(s1)
        k=len(s1)  
        for i in range(len(s2)):
            str1= s2[i:i+k]
            dict2=Counter(str1)
            
            if dict1==dict2:
                return True
        return False
