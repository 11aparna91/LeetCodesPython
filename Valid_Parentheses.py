class Solution:
    def isValid(self, s: str) -> bool:
        Open_Brackets=['(','{','[']
        Closed_Brackets=[')','}',']']
        
        Stack=[]
        
        for i in s:
            if(i in Open_Brackets):
                Stack.append(i)
            else:
                pos=Closed_Brackets.index(i)
                if(len(Stack)>0 and Open_Brackets[pos]==Stack[len(Stack)-1]):
                    Stack.pop()
                else:
                    return False        
        if (len(Stack)==0):
            return True
        else:
            return False
           
        
