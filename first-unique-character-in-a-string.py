class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict1={}
        for i in s:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
        print(dict1)
        for j in dict1:
            if dict1[j]==1:
                return s.index(j)
        return -1

   ################################# Another Solution ########################################
  
  
  
    class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        # build hash map : character and how often it appears
        count = collections.Counter(s)
        
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1        
        
