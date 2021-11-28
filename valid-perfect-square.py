class Solution:
    def isPerfectSquare(self, num: int) -> bool:
      
        if num==1:
            return True
        low=1
        print (low)
        high=int(num/2)
        print (high)
        while low<=high:
            mid=int((low+high)/2)
            square=mid*mid
            if square==num:
                return True
            elif square < num:
                low=mid+1   
            else:
                high=mid-1
        return False
    
    
    
    
