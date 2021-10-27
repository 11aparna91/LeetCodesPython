class Solution:
    def mySqrt(self, x: int) -> int:
        low=0
        high=x
        middle= (low+high)//2
        while(high>middle and middle>low):
            square=middle*middle
            if (square==x):
                return int(middle)
            if (square>x):
                high=middle
            else:
                 low=middle
            middle=(low+high)//2
        if x<high*high:     #check this condition for x=8 or x=1
            return int(low)
        else:
            return int(high)    
            
        
            
        
        
