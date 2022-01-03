class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        str1=""
        for i in range(len(digits)):
            str1= str1 + str(digits[i])
        
        str1=int(str1)
        str1= str1+1
        str1=str(str1)
        output=[]
        
        for i in range(len(str1)):
            output.append(str1[i])
        
        return output
