class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr=[]
        for i in range (0,numRows,1):
            array=[]
            for j in range(0,i+1,1):
                if j==0 or j==i:
                    array.append(1)
                else:
                    array.append(arr[i-1][j-1] + arr[i-1][j])
            arr.append(array)
        return arr
