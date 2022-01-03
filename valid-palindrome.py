class Solution:
    def isPalindrome(self, s: str) -> bool:
        sup= s.lower()
        new=""
        for i in sup:
            if i.isalnum():
                new= new + i
        sup=new
        
        ptr1=0
        ptr2=len(sup)-1
        flag=1
        while ptr1<ptr2:
            if sup[ptr1] == sup[ptr2]:
                ptr1+=1
                ptr2-=1
                continue
            else:
                flag=0
                break
        
        if flag == 1:
            return True
        else:
            return False
