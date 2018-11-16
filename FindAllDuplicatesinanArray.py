from collections import Counter

class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        return [key for (key,value) in Counter(nums).items() if value == 2]
