class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        # nums.sort()
        # target = 1

        # for num in nums:
        #     if num == target:
        #         target += 1

        # return target

        # 原地哈希法：长度为n的数组，缺失的数只会在 [1, n+1] 中出现
        # 把 [1, n] 范围内的数组摆放到对应的位置
        n = len(nums)

        for i in range(n):
            while 0 < nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                target = nums[i] - 1
                nums[i], nums[target] = nums[target], nums[i]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1