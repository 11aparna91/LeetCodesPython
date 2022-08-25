# Problem 190 ######
class Solution:
    def reverseBits(self, n: int) -> int:
        reverse=0
        for i in range(32):
            bit=(n>>i) & 1
            reverse= reverse | ( bit<< (31-i))
        return reverse
        
        
