##########Problem Number 202###################################################################
############# Time Complexity= O(log N) and space complexity= O(log N) #########################
class Solution:
    def isHappy(self, n: int) -> bool:
        
        def get_next(n):
            total=0
            while n > 0:  
                n, m=divmod(n,10)
                total += (m**2)
            return total
        
        visited=set()
        while n!=1 and n not in visited:
            visited.add(n)
            n= get_next(n)
        return n==1
    
   
