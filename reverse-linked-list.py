#########################################Problem 206###############################
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev=None
        while head:
            cur=head
            head=head.next
            cur.next=rev
            rev=cur
        return rev
       
