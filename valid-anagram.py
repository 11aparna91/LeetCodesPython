class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        
        list1=list(s)
        dict1={}
        
        for i in list1:
            if i in dict1:
                dict1[i]+=1
            else:
                dict1[i]=1
        
        print(dict1)
        
        list2=list(t)
        dict2={}
        for i in list2:
            if i in dict2:
                dict2[i]+=1
            else:
                dict2[i]=1
                
        print(dict2)
        
        if dict1==dict2:
            return True
        else:
            return False
