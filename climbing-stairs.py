
########## Problem Number 70 ################
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 1]
        for i in range(2, n + 1):
            dp.insert(i, dp[i - 1] + dp[i - 2])
            
        return dp[n] 
    
###### Time and space complexity for both the solutions in O(n) ###########
### Solution 1 ############
class Solution(object):
    def climbStairs(self, n):
        memo ={}
        memo[1] = 1
        memo[2] = 2
        for i in range(3,n+1):
            memo[i]= memo[i-1] + memo[i-2]
        return memo[n]
      
      
### Solution 2 #############



class Solution(object):
    def climbStairs(self, n):
        memo ={}
        memo[1] = 1
        memo[2] = 2
        
        def climb(n):
            if n in memo: 
                return memo[n]
            else:   
                memo[n] =  climb(n-1) + climb(n-2)
                return memo[n]
        
        return climb(n)


