class Solution:
    def water(self,nums:list[int],a:int,b:int) -> int:
        return (b-a)*min(nums[a],nums[b])
    
    def maxArea(self, height: list[int]) -> int:
        left,right=0,len(height)-1
        max_area=0

        while left<right:
            area=self.water(height,left,right)
            if area>max_area:
                max_area=area

            if height[left]<height[right]:
                left+=1
            else:
                right-=1

        return max_area