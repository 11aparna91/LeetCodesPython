###### Solution 1 Time complexity= O(log N) #########################
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        self.nums, self.target = nums, target
        return self.helper(0, len(nums)-1)
    
    def helper(self, low: int, high: int) -> int:
        if low > high: return -1
        mid = (high + low) // 2
        
        if self.target == self.nums[mid]: return mid
        elif self.target < self.nums[mid]: return self.helper(low, mid-1)
        else: return self.helper(mid+1, high)
        
 ############################## Solution 2  Time complexity= O(log N)  Space Complexity= O(1)#####################

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        
        while(left<=right):
            mid= (left+right)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left=mid+1
            if nums[mid] > target:
                right=mid-1
        return -1
                
            
        
        
