############ Problem Number 1347 ##############
from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnt1=Counter(s)
        cnt2=Counter(t)
        sum=0
        for key,value in cnt1.items():
            if value>cnt2[key]:
                sum += (value - cnt2[key])
        return sum
