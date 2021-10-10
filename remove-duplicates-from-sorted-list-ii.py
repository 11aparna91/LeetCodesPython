# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        if head.next.val!= head.val:
            head.next=self.deleteDuplicates(head.next)
            return head
            
        cur=head
        while cur.next and cur.next.val==head.val:
            cur=cur.next
        return self.deleteDuplicates(cur.next)
                
        
