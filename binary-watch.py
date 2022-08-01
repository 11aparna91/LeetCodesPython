class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        arr=[]
        
        for i in range(12):
            for j in range(60):
                if (bin(i)+bin(j)).count('1') == turnedOn:
                    arr.append(f'{i}:{j:02d}')
        return arr
