################# Problem Number 409 ###########
from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans=0
        for v in Counter(s).values():
            ans += v//2 * 2
            if v%2==1 and ans%2==0:
                ans +=1
        return ans
 ######### Time complexity=O(n) space complexity=O(1) #########
            
