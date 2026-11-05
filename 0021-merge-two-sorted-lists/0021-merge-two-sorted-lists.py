# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: ListNode | None, list2: ListNode | None
    ) -> ListNode | None:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        p1 = list1
        p2 = list2

        if p1.val <= p2.val:
            head = p1
            p1 = p1.next
        else:
            head = p2
            p2 = p2.next

        p = head
        while p1 is not None and p2 is not None:
            if p1.val <= p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next

        if p1 is not None:
            p.next = p1
        if p2 is not None:
            p.next = p2

        return head
