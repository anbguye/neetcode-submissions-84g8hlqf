class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        curr1, curr2 = l1, l2
        dummy = curr = ListNode(0)

        while curr1 or curr2 or carry:
            v1 = curr1.val if curr1 else 0
            v2 = curr2.val if curr2 else 0
            
            temp_total = v1 + v2 + carry
            carry = temp_total // 10
            curr.next = ListNode(temp_total % 10)
            
            curr = curr.next
            if curr1: curr1 = curr1.next
            if curr2: curr2 = curr2.next
        
        return dummy.next