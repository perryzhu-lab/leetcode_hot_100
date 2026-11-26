# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        # nodes = []

        # def dfs(node: TreeNode):
        #     if node is None:
        #         return
        #     nodes.append(node)
        #     dfs(node.left)
        #     dfs(node.right)

        # dfs(root)

        # if len(nodes) == 0 or len(nodes) == 1:
        #     return
        # for i in range(1, len(nodes)):
        #     nodes[i - 1].left = None
        #     nodes[i - 1].right = nodes[i]

        # nodes[-1].left = None
        # nodes[-1].right = None

        curr = root
        while curr is not None:
            if curr.left is not None:
                node = curr.left
                while node.right is not None:
                    node = node.right
                node.right = curr.right
                curr.right = curr.left
                curr.left = None
            curr = curr.right
