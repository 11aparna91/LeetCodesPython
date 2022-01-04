class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        str1=""
        for i in num:
            str1 = str1 + str(i)
        print(str1)
        
        str1= int(str1)
        str1= str1 + k
        
        str1= str(str1)
        output=[]
        for i in str1:
            output.append(i)
        return output
