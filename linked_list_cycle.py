# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        slow = head
        fast = head.next
        if slow==None or fast == None:
            return False
        while(slow!=fast):
            if fast == None or fast.next == None : return False
            slow = slow.next
            fast = fast.next.next
            if fast==pos or slow ==pos:
                return False
        
        return True
