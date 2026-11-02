# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        p=head
        tmp=[]
        while p is not None:
            tmp.append(p.val)
            p=p.next

        for i in range(len(tmp)//2):
            if tmp[i] != tmp[len(tmp)-i-1]:
                return False

        return True
