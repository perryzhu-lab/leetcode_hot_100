from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        # p = head
        # dummy=Node(0,None,None)
        # q=dummy
        # mapping={}
        # while p is not None:
        #     new_node=Node(p.val,None,None)
        #     mapping[p]=new_node
        #     q.next=new_node
        #     q=new_node
        #     p=p.next
        # p=head
        # q=dummy.next
        # while p is not None:
        #     node=p.random
        #     if node is not None:
        #         q.random=mapping[node]
        #     p=p.next
        #     q=q.next
        # return dummy.next

        # 节点交织法
        p=head
        while p is not None:
            new_node=Node(p.val)
            new_node.next=p.next
            p.next=new_node
            p=p.next.next
        p=head
        while p is not None:
            if p.random is not None:
                p.next.random=p.random.next
            p=p.next.next
        if head is None:
            return None
        new_head=head.next

        p=head
        while p is not None:
            q=p.next
            next_node=q.next

            p.next=next_node
            if next_node is not None:
                q.next=next_node.next

            p=next_node

        return new_head