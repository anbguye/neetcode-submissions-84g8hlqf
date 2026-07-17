# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow.next
        prev = slow.next = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        head_1, head_2 = head, prev

        while head_2:

            temp_1, temp_2 = head_1.next, head_2.next
            head_1.next = head_2
            head_2.next = temp_1
            head_1, head_2 = temp_1, temp_2



