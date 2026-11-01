class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         continue
        #     # nums[i]是0  向后找第一个非零nums[j]
        #     j=i+1
        #     while  j<len(nums) and nums[j]==0:
        #         j+=1
        #     if j>=len(nums):
        #         break
        #     nums[i],nums[j]=nums[j],nums[i]

        slow=0
        for fast in range(len(nums)):
            if nums[fast] !=0:
                nums[slow]=nums[fast]
                slow+=1
        for i in range(slow,len(nums)):
            nums[i]=0
