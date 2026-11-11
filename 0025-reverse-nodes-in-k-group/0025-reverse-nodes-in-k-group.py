# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head, k):
        prev_node = None
        curr = head
        group_tail = head

        for i in range(k):
            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node

        group_head = prev_node
        return group_tail, group_head, curr

    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        if k <= 1:
            return head

        dummy = ListNode(0, next=head)
        prev_group_tail = dummy

        curr = head
        length = 0
        while curr is not None:
            length += 1
            curr = curr.next

        for _ in range(length // k):
            curr = prev_group_tail.next

            group_tail, group_head, curr = self.reverseList(curr, k)

            prev_group_tail.next = group_head
            prev_group_tail = group_tail
            group_tail.next = curr

        return dummy.next
