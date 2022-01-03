class Solution:
     def addBinary(self, a: str, b: str) -> str:
            l1=list(a)
            l2=list(b)
            carry=0
            res=""
            sum=0
            while(l1 or l2 or carry):
                if l1:
                    carry = carry + int(l1.pop()) 
                if l2:
                    carry = carry + int(l2.pop())
                out=carry%2
                res= res + str(out)
                carry=carry//2
            return res[::-1]
              
    
    
        
