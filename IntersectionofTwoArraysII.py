class Solution:
    def intersect(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        results=[]
        for i in set(nums1+nums2):
            results.extend([i]*min(nums1.count(i),nums2.count(i)))
        return results
