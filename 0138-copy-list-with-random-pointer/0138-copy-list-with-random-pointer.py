from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        p = head
        dummy=Node(0,None,None)
        q=dummy
        mapping={}
        while p is not None:
            new_node=Node(p.val,None,None)
            mapping[p]=new_node
            q.next=new_node
            q=new_node
            p=p.next
        p=head
        q=dummy.next
        while p is not None:
            node=p.random
            if node is not None:
                q.random=mapping[node]
            p=p.next
            q=q.next
        return dummy.next
    