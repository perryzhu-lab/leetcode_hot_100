# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # nums = []
        cnt = 0
        ans = 0

        def dfs(node: TreeNode):
            nonlocal cnt, ans
            if node is None:
                return
            dfs(node.left)
            if cnt == k:
                return

            cnt += 1
            if cnt == k:
                ans = node.val
                return

            dfs(node.right)

        dfs(root)
        return ans
