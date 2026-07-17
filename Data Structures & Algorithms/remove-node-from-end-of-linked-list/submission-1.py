# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next

        target_length = length - n

        if target_length == 0:
            return head.next

        curr = head
        while target_length > 1 and curr:
            target_length -= 1
            curr = curr.next
        
        if curr and curr.next:
            curr.next = curr.next.next

        return head