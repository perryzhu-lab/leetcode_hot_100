# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import Optional
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # s = set()
        # p = head
        # while p is not None:
        #     if p in s:
        #         return p
        #     s.add(p)
        #     p = p.next
        # return None
        """
        快慢指针法：
        定义：
        a:从 head 到环入口的距离
        b:从环入口到快慢指针相遇点的距离
        c:从相遇点再到环入口的距离

        当 slow 和 fast 第一次相遇的时候:
        slow 走过 s 步, fast 走过 f 步
        则  f = 2s
        fast 比 slow 多走的路必然是环长度的整数倍
        f - s = k(b + c)
        s = k(b + c)
        a + b = k(b + c)
        a = (k - 1)(b + c) + c
        即：
        从头节点走 a 步，可以到达环入口
        从相遇点走 a 步，也可以到达环入口，因为多走的整圈不会改变最终位置。
        """
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                p1=head
                p2=slow
                while p1 is not p2:
                    p1=p1.next
                    p2=p2.next
                return p1

        return None
        
