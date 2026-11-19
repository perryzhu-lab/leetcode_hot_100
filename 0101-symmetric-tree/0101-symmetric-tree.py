# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def check(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val != right.val:
            return False
        if self.check(left.left, right.right) and self.check(left.right, right.left):
            return True
        return False

    def isSymmetric(self, root: TreeNode | None) -> bool:
        if root is None:
            return True
        return self.check(root.left, root.right)
