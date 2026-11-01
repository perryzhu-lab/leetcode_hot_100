class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals:
            return []
        # 按照左端点排序
        intervals.sort(key=lambda x:x[0])

        merged=[intervals[0]]

        for cur_interval in intervals[1:]:
            l=cur_interval[0]
            r=cur_interval[1]

            last_merged=merged[-1]
            last_l=last_merged[0]
            last_r=last_merged[1]

            # 重叠
            if l<=last_r:
                new_end=max(r,last_r)
                merged[-1][1]=new_end

            # 没有重叠
            else:
                merged.append([l,r])
        return merged
