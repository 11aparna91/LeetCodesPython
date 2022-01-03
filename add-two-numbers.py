# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str1=""
        str2=""
        
        while l1:
            str1= str1 + str(l1.val)
            l1=l1.next
        
        str1=str1[::-1]
        
        while l2:
            str2= str2 + str(l2.val)
            l2=l2.next
        
        
        str2=str2[::-1]
        
        sum= int(str1) + int(str2)
        
        sum=str(sum)
        sum=sum[::-1]
        
        head=None
        temp=None
        i=0
        while(i<len(str2)):
            if head is None:
                head= ListNode(sum[i])
                temp= head
            else:
                temp.next= ListNode(sum[i])
                temp=temp.next
            i+=1    
        return head
