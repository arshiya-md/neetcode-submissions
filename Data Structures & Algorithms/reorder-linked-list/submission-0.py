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
        
        temp = slow.next
        slow.next = None #Cut the link to make two halves
        prev = None
        while temp:
            nxt = temp.next
            temp.next = prev
            prev = temp
            temp = nxt

        first, second = head, prev
        while second:
            t1, t2 = first.next, second.next 
            first.next = second
            second.next = t1
            first, second = t1, t2
                

