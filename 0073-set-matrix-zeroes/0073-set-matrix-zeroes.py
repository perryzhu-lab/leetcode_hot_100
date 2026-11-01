class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])

        # 记录第0行 和 第0列 是否有0
        zero_row = False
        zero_col = False

        # 检查第0行和第0列是否有0
        for j in range(col):
            if matrix[0][j] == 0:
                zero_row = True
        for i in range(row):
            if matrix[i][0] == 0:
                zero_col = True

        for i in range(1,row):
            for j in range(1,col):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1,row):
            for j in range(1,col):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        if zero_row:
            for i in range(col):
                matrix[0][i] = 0

        if zero_col:
            for i in range(row):
                matrix[i][0] = 0