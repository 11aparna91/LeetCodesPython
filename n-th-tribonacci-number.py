class Solution:
    def tribonacci(self, n):
        memo={}
        memo[0]=0
        memo[1]=1
        memo[2]=1
        
        for i in range(3,n+1):
            memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
        return memo[n]
      
      
######### Solutin 2 #########

class Solution:
    def tribonacci(self, n):
        arr = [0,1,1]
        if n <= 2:
            return arr[n]
        for i in range(3,n+1):
            arr.append(arr[i-1]+arr[i-2]+arr[i-3])
        return arr[n]
