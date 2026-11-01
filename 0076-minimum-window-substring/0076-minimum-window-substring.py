from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 存储t中每个字符需要的数量
        dict_t=defaultdict(int)
        # 存储当前窗口内t相关字符的数量
        dict_window=defaultdict(int)

        # 统计t需要的字符
        for c in t:
            dict_t[c]+=1
        
        left=0

        # 记录窗口中满足dict_t数量的字符种类数
        valid=0
        # 记录最小子串起始下标
        start=0
        # 记录最小子串长度，初始为无穷大
        min_len=float('inf')

        # 右边界遍历
        for right in range(len(s)):
            c=s[right]
            # c是t需要的
            if c in dict_t:
                dict_window[c]+=1
                # 判断有效种类
                if dict_window[c]==dict_t[c]:
                    valid+=1

            # 收缩左边界
            while valid==len(dict_t):
                # 更新最小子串
                cur_len = right-left+1
                if cur_len <min_len:
                    min_len=cur_len
                    start=left

                # 左边界右移
                d = s[left]
                left+=1

                # 如果被移除的是t需要的
                if d in dict_t:
                    if dict_window[d]==dict_t[d]:
                        valid-=1
                    dict_window[d]-=1

        if min_len==float("inf"):
            return ""
        else:
            return s[start:start+min_len]
            
            
                

