class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        letters = [i for i in "abcdefghijklmnopqrstuvwxyz"]
        dict1=dict(zip(letters,widths))
        translation = [dict1.get(i) for i in S]

        runningtot=0
        nlines=0
        for i in translation:
            runningtot += i
    
            if runningtot > 100:
                nlines += 1
                runningtot = i

        if runningtot > 0:
            return [nlines+1,runningtot]
        else:
            return [nlines,0]
