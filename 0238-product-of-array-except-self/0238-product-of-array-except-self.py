from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # ans=[]
        # n=len(nums)
        # # 记录前缀积和后缀积
        # left=[1]*n
        # right=[1]*n

        # for i in range(1,n):
        #     left[i]=left[i-1]*nums[i-1]
        # for i in range(n-2,-1,-1):
        #     right[i]=right[i+1]*nums[i+1]

        # for i in range(n):
        #     ans.append(left[i]*right[i])

        # return ans

        # 优化版本
        n=len(nums)
        ans=[1]*n

        # ans 先暂存前缀积
        for i in range(1,n):
            ans[i] = ans[i-1] * nums[i-1]

        right_product=1
        for i in range(n-1,-1,-1):
            ans[i] *= right_product
            right_product *= nums[i]

        return ans