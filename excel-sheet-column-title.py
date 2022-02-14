import string
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        alphabet=string.ascii_uppercase
        result=""
        
        while columnNumber>0:
            columnNumber -= 1
            columnNumber,r =divmod(columnNumber,26)
            result += alphabet[r]
        
        return result[::-1]
            
        
   
