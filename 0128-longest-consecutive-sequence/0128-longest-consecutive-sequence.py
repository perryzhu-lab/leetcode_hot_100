class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # 边界处理：数组为空  返回0
        if not nums:
            return 0
        # 构建哈希集合  自动去重
        num_set=set(nums)
        max_len=0
        # 遍历哈希集合里的每一个数字
        for num in num_set:
            # 判断是否为起点  是起点则展开计算
            if num-1 not in num_set:
                cur=num
                cur_len=1
                while(cur+1 in num_set):
                    cur+=1
                    cur_len+=1
                max_len=max(max_len,cur_len)
        return max_len