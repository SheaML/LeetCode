class Solution:
    def trap(self, height: List[int]) -> int:
        
        if len(height) < 2:
            return 0
        
        counts=[]
        for i in range(1,len(height)):
            counts.append(min(max(height[i:]),max(height[:i])) - height[i])
        
        counts=[0 if i<0 else i for i in counts]
        return sum(counts)
            
