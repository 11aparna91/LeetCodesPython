class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        total=0
        multiply=1
        for i in range(len(digits)-1,-1,-1):
            d= digits[i]
            multiply=multiply*1
            total= total + (d*multiply)
            multiply=multiply*10
        total= total + 1    
        res = [int(x) for x in str(total)]
        return res    
        
