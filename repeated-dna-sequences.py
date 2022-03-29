# Problem Number: 187
# Time complexity: O((N-l)l)
# Space Complexity: O((N-l)l)

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        n=len(s)
        l=10
        all_str=set()
        output= set()
        for i in range(n-l+1):
            temp= s[i:i+l]
            if temp in all_str:
                output.add(temp)
            all_str.add(temp)
        return output
