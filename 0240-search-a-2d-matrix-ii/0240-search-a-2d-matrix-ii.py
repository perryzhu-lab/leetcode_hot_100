from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        # # 暴力解法
        # for i in range(m):
        #     for j in range(n):
        #         if target==matrix[i][j]:
        #             return True
        # return False
        # # 方法二
        # for i in range(m):
        #     if target < matrix[i][0]:
        #         break
        #     for j in range(n):
        #         if target < matrix[i][j]:
        #             break
        #         if target == matrix[i][j]:
        #             return True
        # return False
        # 方法三
        i=0
        j = n-1
        while i<m and j>=0:
            if matrix[i][j]==target:
                return True
            elif matrix[i][j]<target:
                i+=1
            else:
                j-=1
        return False