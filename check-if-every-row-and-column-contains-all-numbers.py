import math
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        leng= len(matrix)        
        for i in range(leng):
            num=1
            while(num<=leng):
                if num in  matrix[i]:
                    num=num+1
                else:
                    return False
                
        if leng==1:
            if len(matrix[0])==1:
                return True
            else:
                return False
        
        else:
            sum_i= math.floor(leng*(leng+1)/2)
            print(sum_i)
            
            cnt=0
            for i in range(leng):
                total=0
                total_col=0
                
                for j in range(leng):
                    total=total + matrix[i][j]
                    total_col= total_col + matrix[j][i]
                if (total==sum_i and total_col==sum_i):
                    cnt=cnt+1
                else:
                    return False
            print(cnt,leng)
            if cnt==leng:
                return True
            else: 
                return False
  ############################################################################# Another Solution with constant space##############################################
  ##########################################you can use sum of elements to check along with no repeating elements anywhere to avoid the edge case#################
  class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        s = (n*(n+1))//2
        for row in range(n):
            if n>1 and matrix[row][0]==matrix[row][1]:
                return False
            if sum(matrix[row])!=s:
                return False
        for column in range(n):
            ss=0
            for row in range(n):
                ss+=matrix[row][column]
            if ss!=s:
                return False
        return True
