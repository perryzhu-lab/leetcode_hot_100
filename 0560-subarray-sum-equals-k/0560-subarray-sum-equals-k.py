from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp={0:1}
        cur=0
        res=0

        for num in nums:
            cur+=num
            res+=mp.get(cur-k,0)
            mp[cur]=mp.get(cur,0)+1

        return res