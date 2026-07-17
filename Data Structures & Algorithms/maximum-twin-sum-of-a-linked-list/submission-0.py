# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        slow, fast = head, head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

        curr = slow
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        head_1, head_2 = head, prev
        res = 0
        while head_1 and head_2:

            res = max(res, head_1.val + head_2.val)
            head_1 = head_1.next
            head_2 = head_2.next
        
        return res
