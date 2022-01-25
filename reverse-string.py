class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        length=len(s)
        ptr1=0
        ptr2=len(s)-1
        
        for i in range(length//2):
            temp=s[ptr1]
            s[ptr1]=s[ptr2]
            s[ptr2]=temp
            ptr1+=1
            ptr2-=1
            i+=1
     
 ####################################################Solution 2####################################
class Solution:
    def reverseString(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1
