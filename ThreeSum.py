class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        from collections import Counter
        nums.sort()
        counts=Counter(nums) 
        a,b = set(),set()
        for i in nums:
            counts[i] -= 1
            for x in a:
                if counts[-(i+x)] > 0:
                    b.add((i,x,-(i+x)))
            a.add(i)
        return list(b)
