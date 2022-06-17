### Time complexity= O(n) space complexity=O(1) #########
#######  Problem Number 412 #################
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        lis=[]
        for i in range(1,n+1):
            if i%3==0 or i%5==0:
                if i%5==0 and i%3==0:    
                    lis.append("FizzBuzz")
                else:    
                    if i%3==0:
                        lis.append("Fizz")
                    if i%5==0:
                        lis.append("Buzz")
                
            else:
                lis.append(str(i))
        return lis
                
        
        
