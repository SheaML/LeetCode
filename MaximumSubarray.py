class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curSum=maxSum=nums[0]
        
        for i in nums[1:]:
            
#consider max sum ending at that position. could be just that number or the maximum so far + that number
            curSum=max(i,curSum+i)
#compare to global
            maxSum=max(maxSum,curSum)
        
        return maxSum
