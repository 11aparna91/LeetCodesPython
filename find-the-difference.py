class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        extra={}
        for i in t:
            if i in extra:
                extra[i]+=1
            else:
                extra[i]=1
        for i in s:
            if i in extra:
                extra[i]-=1
        for i in extra:
            if extra[i]==1:
                return i
        
