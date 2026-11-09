# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        # 两次遍历法
        # if head is None:
        #     return None
        # len = 0
        # p = head
        # while p is not None:
        #     len += 1
        #     p = p.next

        # index = len - n + 1

        # if index == 1:
        #     return head.next

        # i = 1
        # p = head

        # while i < index - 1:
        #     i += 1
        #     p = p.next

        # p.next = p.next.next
        # return head

        # 快慢指针法
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy
        # fast先走n+1步
        i = 0
        while i < n + 1:
            i += 1
            fast = fast.next
        
        while fast is not None:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next
