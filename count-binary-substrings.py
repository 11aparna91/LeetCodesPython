###############Problem Number 696 ########################################
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev,curr,ans= 0, 1, 0
        for i in range(len(s)-1):
                if s[i]!=s[i+1]:
                    ans= ans + min(prev,curr)
                    prev= curr
                    curr=1
                
                else:
                    curr +=1
        return ans + min(prev,curr)
      
######################## Time Complexity= O(n) and Space Complexity=O(1)######
