class Solution:
    def pivotIndex(self, nums: 'List[int]') -> 'int':
        
        S=sum(nums)
        
        for i in range(len(nums)):
            sum1= sum(nums[:i])
            if sum1 == S - sum1 - nums[i]:
                return i
        return -1
