class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea=0
        i=0
        j=len(height)-1
        
        maxarea=min(height[i],height[j])*(j-i)

        while i < j:
            if height[i] < height[j]:
                i+=1
            else:
                j-=1
            maxarea=max(maxarea,min(height[i],height[j])*(j-i))
        return maxarea
