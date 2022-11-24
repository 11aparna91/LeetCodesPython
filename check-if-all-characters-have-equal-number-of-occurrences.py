####### Problem Number 1941 ##############
from collections import Counter
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        dict1=Counter(s)
        print(dict1)
        print(Counter(s).values())
        set1=set(Counter(s).values())
        
        if len(set(Counter(s).values()))==1:
            return True
        else:
            return False
        print(set1)
