class Solution:
    def checkString(self, s: str) -> bool:
          
        char1='a'
        char2='b'
        count=0
        index_a=0
        index_b=101
        
        if char1 not in s:
            return True
        
        if char2 not in s:
            return True
        
        for i in range(len(s)):
            if s[i]==char1:
                if (i>index_a):
                    index_a=i
            if s[i]==char2:
                if (i<index_b):
                    index_b=i
        
        print(index_a,index_b)
        if index_b>index_a:
            return True
        else:
            return False
         
             
            
