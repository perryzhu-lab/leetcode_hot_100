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
        tag = False
        head = ListNode(0, None)
        p = head
        while p1 is not None or p2 is not None:
            v1=p1.val if p1 is not None else 0
            v2=p2.val if p2 is not None else 0
            if tag is True:
                value = v1 + v2 + 1
                if value < 10:
                    tag = False
            else:
                value = v1 + v2
                if value >= 10:
                    tag = True
            new_node = ListNode(val=value % 10, next=None)
            p.next = new_node
            p = p.next
            if p1 is not None:
                p1 = p1.next
            if p2 is not None:
                p2 = p2.next


        if tag is True:
            new_node=ListNode(val=1,next=None)
            p.next=new_node

        return head.next
