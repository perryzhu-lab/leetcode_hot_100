class Solution:
    def trap(self, height: list[int]) -> int:
        res=0
        l_max,r_max=0,0

        l,r=0,len(height)-1
        while l<=r:
            # 更新l_max r_max
            if l_max<height[l]:
                l_max=height[l]
            if r_max<height[r]:
                r_max=height[r]
            if l_max<r_max:
                res+=l_max-height[l]
                l+=1
            else:
                res+=r_max-height[r]
                r-=1
        return res
    