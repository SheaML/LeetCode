class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words=s.split(" ")
        words=[i for i in words if i]
        
        res=(words or [None])[-1]
        if res is None:
            return 0
        else:
            return len(res)
    
