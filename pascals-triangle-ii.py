#Problem Number 119
#Solution Number 1
import numpy
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rows, cols=(rowIndex+1,rowIndex+1)
        arr= [[0 for i in range(cols)] for j in range(rows)]
        
        for i in range(rowIndex+1):
            for j in range(rowIndex+1):
                if j==0 or j==rowIndex or i==0:
                    if j==0 or j==rowIndex:
                        arr[i][j]=1
                    else:
                        arr[i][j]=0
                else:
                    arr[i][j]=arr[i-1][j] + arr[i-1][j-1]
        return arr[rowIndex]

#############################################################
############################################# Solution Number 2 ######################################################

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
        prev_row= self.getRow(rowIndex-1)
        middle=[]
        
        for i in range(len(prev_row)-1):
            middle.append(prev_row[i] + prev_row[i+1])
        
        
        return [1] + middle + [1]
