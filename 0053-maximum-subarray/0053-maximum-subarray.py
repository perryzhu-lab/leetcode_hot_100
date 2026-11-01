class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # 记录当前位置结尾的连续子数组的最大和
        cur_sum=nums[0]
        # 记录全局最大的子数组和
        ans=nums[0]

        for i in range(1,len(nums)):
            num=nums[i]

            option1=cur_sum+num
            option2=num

            cur_sum=max(option1,option2)

            if cur_sum>ans:
                ans=cur_sum

        return ans