from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q=deque()
        ans=[]

        for i,val in enumerate(nums):
            # 不断从队尾弹出小于等于新元素的值
            while q and nums[q[-1]]<=val:
                q.pop()
            # 当前下标入队
            q.append(i)

            # 检查队首
            while q[0]<=i-k:
                q.popleft()

            # 窗口成型收集最大值
            if i>=k-1:
                ans.append(nums[q[0]])


        return ans