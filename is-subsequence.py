# Problem Number 392

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        LEFT_BOUND, RIGHT_BOUND= len(s),len(t)
        ptr1=ptr2=0
        
        while ptr1<LEFT_BOUND and ptr2<RIGHT_BOUND:
            if s[ptr1]==t[ptr2]:
                ptr1 +=1
            ptr2 +=1
        return ptr1==LEFT_BOUND
        
        
################## Solution 2 Using Greedy Algorithm i.e Divide and conquer #######################################
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        LEFT_BOUND, RIGHT_BOUND= len(s),len(t)
        
        
        def rec_isSubsequence(left_index, right_index) -> bool:
            if left_index==LEFT_BOUND:
                return True
            if right_index==RIGHT_BOUND:
                return False
            if s[left_index]==t[right_index]:
                left_index +=1
            right_index +=1
        
            return rec_isSubsequence(left_index, right_index)
        
        
        return rec_isSubsequence(0,0)
    
        
        


