# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        # # 暴力解法
        # p1 = headA

        # while p1 is not None:
        #     p2 = headB
        #     while p2 is not None:
        #         if p2 is p1:
        #             return p2
        #         p2 = p2.next
        #     p1 = p1.next

        # # 尾部对齐法
        # p1 = headA
        # p2 = headB
        # m = 0
        # n = 0
        # while p1 is not None:
        #     m += 1
        #     p1 = p1.next
        # while p2 is not None:
        #     n += 1
        #     p2 = p2.next
        # p3 = headA
        # p4 = headB
        # if m > n:
        #     step = m - n
        #     for _ in range(step):
        #         p3 = p3.next
        # else:
        #     step = n - m
        #     for _ in range(step):
        #         p4 = p4.next
        # while p3 is not p4:
        #     p3 = p3.next
        #     p4 = p4.next
        # return p3

        # 双指针切换法
        p1 = headA
        p2 = headB
        while p1 is not p2:
            if p1 is None:
                p1 = headB
            else:
                p1=p1.next
            if p2 is None:
                p2 = headA
            else:
                p2 = p2.next
        return p1
