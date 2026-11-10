# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        if head is None or head.next is None:
            return head
        dummy=ListNode(0,head)
        p=dummy
        
        while p.next is not None and p.next.next is not None:
            q=p.next
            r=q.next
            p.next=r
            q.next=r.next
            r.next=q
            p=q

        return dummy.next
        