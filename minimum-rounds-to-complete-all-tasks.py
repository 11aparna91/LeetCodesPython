#### Problem Number 2244 Time Complexity= O(n) ##########
from collections import Counter
from typing import List
import math
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        def total(cnt):
            rem=cnt%3
            div=cnt//3
            
            if rem ==0: return div
            else: return div + 1
        
        count= Counter(tasks)
        
        ans=0
        for key,val in count.items():
            if val==1:
                return -1
            else:
                ans +=total(val)
        return ans
        
