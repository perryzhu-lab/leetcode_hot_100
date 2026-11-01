class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        ans = []

        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # 从左到右
            for j in range(left, right + 1):
                ans.append(matrix[top][j])
            top += 1
            if top > bottom:
                break

            # 从上到下
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1
            if left > right:
                break

            # 从右到左
            for j in range(right, left - 1, -1):
                ans.append(matrix[bottom][j])
            bottom -= 1

            # 从下到上
            for i in range(bottom, top - 1, -1):
                ans.append(matrix[i][left])
            left += 1

        return ans
