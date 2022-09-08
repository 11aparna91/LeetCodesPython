class Solution:
    def backspaceCompare(self, S: str,T: str) -> bool:
    	s,t = [],[]
    	for i in S: s = s + [i] if i != '#' else s[:-1]
    	for i in T: t = t + [i] if i != '#' else t[:-1]
    	return s==t
 ##################################################
class Solution(object):
    def backspaceCompare(self, S, T):
        def build(S):
            ans = []
            for c in S:
                if c != '#':
                    ans.append(c)
                elif ans:
                    ans.pop()
            return ans
        return build(S) == build(T)
