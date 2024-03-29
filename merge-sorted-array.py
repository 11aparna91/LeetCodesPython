class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        while (m>0 and n>0):
            if (nums1[m-1]>=nums2[n-1]):
                nums1[m+n-1]=nums1[m-1]
                m=m-1
            else:
                nums1[m+n-1]=nums2[n-1]
                n=n-1        
        if (n>0):   #if the length(nums1)=0, i.e m=0 then return all the elements from list 2 nums1=[0] nums2=[2] this test case is required when there are no numbers in the nums1 
            nums1[:n]=nums2[:n]
   # Problem Number 88 #############
###### Time complexity= O(m +n), Space Complexity= O(1) (need to check) ###################
                        
                
        
        
        
            
                
                    
                
        
