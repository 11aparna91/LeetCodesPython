class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set2=set()
        # created set so that there wont be any duplicates.
        
        l=0 #need two pointers left and right
        res=0 #should return the max length of res
        
        for r in range(len(s)):
            while(s[r] in set2):
                set2.remove(s[l])
                l=l+1
                
            
            set2.add(s[r])
            res= max(res, r-l+1)
        return res
            
            
        
        
