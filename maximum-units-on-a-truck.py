########################## Time Complexity= O(n) and Space Complexity=O(1) #############
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1])
        boxTypes=boxTypes[::-1]
       
        
        total=0
        for i in range(len(boxTypes)):
            if boxTypes[i][0]<=truckSize:
                truckSize -=boxTypes[i][0]
                total= total + (boxTypes[i][0] * boxTypes[i][1])
            else: 
                total = total + (truckSize * boxTypes[i][1])
                break
            
      
        return total            
                  
############################# Solution 2 #########################################     
