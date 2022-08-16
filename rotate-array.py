class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k= k % len(nums)
        res= [0] * len(nums)
        for i in range(len(nums)):
            res [(i+k)%len(nums)] = nums[i]
        
        for i in range(len(nums)):
            nums[i]=res[i]
            
            
##############################################


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k= k % len(nums)
        self.reverse(nums, 0, len(nums)-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, len(nums)-1)
    
    def reverse(self, nums,l,r):
            while l<r:
                nums[l], nums[r] =  nums[r], nums[l]
                l,r= l+1, r-1
            

            
