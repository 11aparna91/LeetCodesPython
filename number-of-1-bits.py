#Problem 191
class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        while n:
            count+=1 
            n &=n-1   # AND with the 1's complement to cancel the rightmost 1
        return count
            
#######################


class Solution:
    def hammingWeight(self, n: int) -> int:
        res=0
        while n:
            res += n%2 #to get the last bit
            n = n>>1   # right shift
        return res
        
