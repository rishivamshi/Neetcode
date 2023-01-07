# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head.next == None:
            return head
        slow, fast = head, head
        
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        temp = head
        while(temp.next != slow):
            temp = temp.next
        temp.next = None
        
        
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        next_head = prev

        temp1 = head
        while(temp1.next != None ):
            a = temp1.next
            b = next_head.next
            temp1.next = next_head
            next_head.next = a
            temp1 = a
            next_head = b
        if next_head != None:
            temp1.next = next_head
