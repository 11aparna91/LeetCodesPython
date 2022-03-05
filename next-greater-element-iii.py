class Solution:
    def nextGreaterElement(self, n: int) -> int:
        arr= list(map(int, str(n)))
        
        i=len(arr)-2
        while i>=0 and arr[i]>=arr[i+1]:
            i -=1        
        if i<0:
            return -1
        
        j=len(arr)-1
        
        while j>=0 and arr[j]<=arr[i]:
            j=j-1
        
        
        arr[i],arr[j] = arr[j], arr[i]
        
        arr[i+1:]=arr[i+1:][::-1]
        
        result=""
        
        for k in arr:
            result = result + str(k)
        result=int(result)
        
        if result > n and result<2**31:
            return result
        else:
            return -1
    
    
    #### Problem Number 556 ###################
    ################ Time complexity = O(n) and space complexity= O(N)
