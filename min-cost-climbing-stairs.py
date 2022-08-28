################## Problem Number 746 #########
############# Time Complexity= O(n) ###########
############# Space Complexity= O(1) ##########

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:          
        for i in range(2, len(cost)):
            cost[i] += min(cost[i-1],cost[i-2])
            print(cost[i])  
        return min(cost[-1],cost[-2])
       
 ###############################################
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(len(cost)-3,-1,-1):
            cost[i] += min(cost[i+1],cost[i+2]) 
        return min(cost[0],cost[1])
            
       
