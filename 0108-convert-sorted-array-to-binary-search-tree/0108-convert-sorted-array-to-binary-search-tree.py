# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        if nums == []:
            return

        root = TreeNode(nums[len(nums) // 2])
        left = nums[: len(nums) // 2]
        right = nums[(len(nums) // 2) + 1 :]

        root.left = self.sortedArrayToBST(left)
        root.right = self.sortedArrayToBST(right)

        return root