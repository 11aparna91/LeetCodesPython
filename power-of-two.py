class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        flag=0
        for i in range(31):
            if (n == pow(2,i)):
                flag=1
                return True
        if flag == 0:
            return False

        
###########################################
#Another Code##############################
def isPowerOfTwo(self, n):
    return (n>0) and (n & (n-1))==0
  
############################################
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==1:
            return True
        res=1
        for i in range(31):
            res = res * 2
            if res==n:
                return True
            if res>n:
                break
        return False
