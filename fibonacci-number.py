#Iterative method
class Solution:
    def fib(self, n: int) -> int:
        first=0
        second=1
        if n<2:
            return n
        for i in range(n-1):
            sumi= first + second
            first = second
            second = sumi
        return sumi
 
# Recursive method

class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        return self.fib(n-1) + self.fib(n-2)
        

      
            
            
        
