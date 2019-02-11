class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashMap = {}
        for i in range(len(nums)):
	        x = nums[i]
	        if x in hashMap:
		        return [hashMap[x], i]
	        else:
		        hashMap[target - x] = i
