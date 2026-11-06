# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        p1 = l1
        p2 = l2
        carry = 0
        head = ListNode(0, None)
        p = head
        while p1 is not None or p2 is not None or carry:
            v1 = p1.val if p1 is not None else 0
            v2 = p2.val if p2 is not None else 0
            value = v1 + v2 + carry
            carry = value // 10
            new_node = ListNode(val=value % 10, next=None)
            p.next = new_node
            p = p.next
            if p1 is not None:
                p1 = p1.next
            if p2 is not None:
                p2 = p2.next

        return head.next
