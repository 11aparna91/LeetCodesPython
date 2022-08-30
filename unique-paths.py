############### Space Complexity=O(m*n) #############
##############  Problem Number 62 ###################
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if not m or not n:
            return 0
        dp = [[1 for i in range(n)] for j in range(m)]
        for i in range(1,m):   ## consider reverse matrix
            for j in range(1,n):
                dp[i][j]= dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
