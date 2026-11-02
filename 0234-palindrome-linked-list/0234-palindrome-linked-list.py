# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # p = head
        # tmp = []
        # while p is not None:
        #     tmp.append(p.val)
        #     p = p.next

        # for i in range(len(tmp) // 2):
        #     if tmp[i] != tmp[len(tmp) - i - 1]:
        #         return False

        # return True

        # 快慢指针+反转链表
        fast = slow = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

        # 反转第二个链表
        p = slow.next
        slow.next = None

        while p is not None:
            q = p.next
            p.next = slow
            slow = p
            p = q

        # 比较链表
        r1 = head
        r2 = slow
        while r1 is not None and r2 is not None:
            if r1.val != r2.val:
                return False
            r1 = r1.next
            r2 = r2.next
        return True
