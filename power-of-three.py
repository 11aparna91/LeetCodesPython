# Time Complexity: O(log n) (base 3)
# Space Complexity: O(1)
# Problem Number 326

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<1:
            return False
        while(n%3==0):
            n /= 3
        
        return n==1
      
      
