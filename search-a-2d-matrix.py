###### TC: O(logm+logn) = O(log(mn)) ###################
#############SC: O(1) ##################################
############# Problem Number 74 ##########################

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=len(matrix)
        col=len(matrix[0])
        low=0
        high= row*col-1
        
        while low<=high:
            mid=(low+high)//2
            l,r =divmod(mid,col)
            if matrix[l][r]==target:
                return True
            elif matrix[l][r] > target:
                high= mid-1
            else:
                low= mid+1
        return False
        
        
        
