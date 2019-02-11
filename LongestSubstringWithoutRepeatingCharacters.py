class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        running=[]
        high=0

        for i in s:
            if i in running:
                running = running[running.index(i) +1:len(running)]
            running.append(i)
            if len(running) > high:
                high = len(running)
        return high
