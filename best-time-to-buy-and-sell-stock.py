######Problem Number 121 ##########################
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]
        max_diff=0
        n=len(prices)
        
        for i in range(n):
            mini=min(mini,prices[i])
            max_diff=max(max_diff,prices[i]-mini)
        return max_diff
            
