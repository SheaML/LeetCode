class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        words=s.split(" ")
        revwords = " ".join([i[::-1] for i in words])
        return revwords

        
