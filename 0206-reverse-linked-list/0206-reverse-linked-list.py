# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        # if head is None:
        #     return None
        # nodes = []
        # p = head
        # while p is not None:
        #     nodes.append(p)
        #     p = p.next
        # for i in range(len(nodes) - 1, 0, -1):
        #     nodes[i].next = nodes[i - 1]
        # nodes[0].next = None
        # return nodes[len(nodes) - 1]

        # if head is None:
        #     return None
        # p = head
        # q = p.next
        # p.next = None

        # while q is not None:
        #     r = q.next
        #     q.next = p
        #     p = q
        #     q = r

        # return p

        if head is None or head.next is None:
            return head
        new_head= self.reverseList(head=head.next)

        head.next.next=head
        head.next=None 
        return new_head
