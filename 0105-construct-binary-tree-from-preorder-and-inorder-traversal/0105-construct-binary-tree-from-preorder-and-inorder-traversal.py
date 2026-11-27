# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        # 1. 递归终止条件
        if not preorder:
            return None

        # 2. 构建根节点
        root = TreeNode(preorder[0])

        # 3. 划分中序遍历
        idx = inorder.index(root.val)
        inorder_left = inorder[:idx]
        inorder_right = inorder[idx + 1 :]

        # 4. 划分前序遍历
        len_left = len(inorder_left)
        preorder_left = preorder[1 : 1 + len_left]
        preorder_right = preorder[1 + len_left :]

        # 5. 递归构建左右子树
        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)

        # 6. 返回根节点
        return root
