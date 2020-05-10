class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        lennum=len(nums)
        for i in range(lennum):
            even=0
            number=nums[i]
            while(number!=0):
               rem=number%10 
               even+=1
               number=int(number/10)
            if even%2==0:
                count+=1
        return count 
        
