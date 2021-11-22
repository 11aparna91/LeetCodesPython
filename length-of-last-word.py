class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        j=0
        i=len(s)-1
        while (s[i]==' '):
            i=i-1
        while (s[i]!=' ' and i>-1):
            j=j+1
            i=i-1                 
        return j    
