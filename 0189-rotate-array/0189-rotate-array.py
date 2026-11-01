class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        # 处理k>n的情况
        k=k%n

        # # 辅助数组法
        # temp=[]
        # for num in nums[n-k:n]:
        #     temp.append(num)
        # for num in nums[0:n-k]:
        #     temp.append(num)
        # nums[:]=temp

        # 三次反转法
        def reverse(left,right):
            while left<right:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right-=1

        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)