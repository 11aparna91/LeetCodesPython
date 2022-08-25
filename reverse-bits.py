# Problem 190 ######
class Solution:
    def reverseBits(self, n: int) -> int:
        reverse=0
        for i in range(32):
            bit=(n>>i) & 1  #(logical AND of ith bit with 1 to get ith bit)
            reverse= reverse | ( bit<< (31-i))  #(result is from 31st place first to 0th later) 
        return reverse
        
        
