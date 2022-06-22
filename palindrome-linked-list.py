############ Problem Number 234 ############
############ Time Complexity=O(n) ##########
############ Space Complexity=O(n) #########
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lis=[]
        temp=head
        while temp is not None:
            lis.append(temp.val)
            temp=temp.next
        if lis==lis[::-1]:
            return True
        else:
            return False
        
    
            
            
