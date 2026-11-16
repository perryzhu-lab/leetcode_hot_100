class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge(self, p1, p2):
        dummy = ListNode(0)
        q = dummy
        q1 = p1
        q2 = p2
        while q1 is not None and q2 is not None:
            if q1.val <= q2.val:
                q.next = q1
                q1 = q1.next
            else:
                q.next = q2
                q2 = q2.next
            q = q.next

        if q1 is not None:
            q.next = q1
        if q2 is not None:
            q.next = q2

        return dummy.next

    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]

        mid = len(lists) // 2
        left = lists[:mid]
        right = lists[mid:]

        left = self.mergeKLists(left)
        right = self.mergeKLists(right)

        return self.merge(left, right)
