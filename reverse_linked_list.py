# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # reverse = []
        # current = head
        # while(head):
        #     reverse.append(head.val)
        #     head = head.next
        # reverse = reverse[::-1]
        # i = 0
        # head = current
        # while(head):
        #     head.val = reverse[i]
        #     i+=1
        #     head=head.next
        # return current
        
        # using recursion
        
        if head==None or head.next == None:
            return head
        
        ans = self.reverseList(head.next)
        k = head.next
        k.next = head
        head.next = None
        return ans

