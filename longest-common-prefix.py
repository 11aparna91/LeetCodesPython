class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
            prefix= strs[0]
            min_list=[]
            len_p=len(prefix)
            print(len_p)
            for s in strs:
                len_s=len(s)
                i=0
                j=0
                while i<len_p and j<len_s:
                    if(prefix[i]!=s[j]):
                        break
                    i=i+1
                    j=j+1
                min_list.append(prefix[:i])
            min_len=len(min_list[0])    
            for s in min_list:
                if len(s)<min_len:
                    min_len=len(s)
            return prefix[:min_len]
            
                
                    
                
            
            
        
