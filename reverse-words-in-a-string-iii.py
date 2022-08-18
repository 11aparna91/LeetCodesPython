#################### Problem Number 557 ################

class Solution:
    def reverseWords(self, s: str) -> str:
        str_splt=s.split(" ")
        str_splt=[i[::-1] for i in str_splt] 
        return " ".join(str_splt)
###########################################################

class Solution:
    def reverseWords(self, s: str) -> str:
        res = ''
        l, r = 0, 0
        while r < len(s):
            if s[r] != ' ':
                r += 1
            elif s[r] == ' ':
                res += s[l:r + 1][::-1]
                r += 1
                l = r
        res +=' '
        res += s[l:r + 1][::-1]
        
        return res[1:]
