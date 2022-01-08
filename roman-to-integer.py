#Problem 13
class Solution:
    def romanToInt(self, s: str) -> int:
        dict1={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}    #Used Dictionary
        
        res=0
        for i in range(0,len(s)-1):
            if dict1[s[i]] < dict1[s[i+1]]:
                res= res - dict1[s[i]]
            else:
                res= res + dict1[s[i]]
        return res + dict1[s[-1]]
            
