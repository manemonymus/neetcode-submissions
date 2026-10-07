class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l=0
        r=len(height)-1
        max_area=0
        while l<r:
            min_height=min(height[l],height[r])
            area=(r-l)*min_height
            if area>max_area:
                max_area=area
            if min_height==height[l]:
                l+=1
            else:
                r-=1
        return max_area


        