class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum=nums[0]
        current_sum=nums[0]
        
        for i in (nums[1:]):
            current_sum= max(i, current_sum + i)
            best_sum=max(best_sum,current_sum)
        return best_sum
