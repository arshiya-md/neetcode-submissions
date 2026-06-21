# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(-1)
        curr = dummy
        carry = 0

        while l1 or l2 or carry:

            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0

            sum_ = num1 + num2 + carry
            l3_val = sum_ % 10
            carry = sum_ // 10

            l3 = ListNode(l3_val)

            curr.next = l3
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
        