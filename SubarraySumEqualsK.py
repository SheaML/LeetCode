class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        from collections import Counter
        
        counts=collections.Counter()
        counts[0] = 1
        count = sum_ = 0
        
        for i in nums:
            sum_+=i
            count+=counts[sum_-k]
            counts[sum_]+=1
        return count
