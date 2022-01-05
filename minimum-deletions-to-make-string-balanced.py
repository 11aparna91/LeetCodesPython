class Solution:
    def minimumDeletions(self, s: str) -> int:
        b_count=0
        dp=[0 for i in range(len(s)+1)]
        
        res=0
        for i in range(len(s)):
            if s[i]=='a':
                # either remove this 'a': res + 1
                # or keep this 'a': bcount (must remove all previous 'b's)
                dp[i+1]=dp[i]
                res=min(res+1, b_count)
            else:
                # Fine for 'b' in the tail
                b_count+=1
       
        return res
        
