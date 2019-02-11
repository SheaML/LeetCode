class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def numbify(s):
            patterndict={}
            count=0
            trans=[]
            for i in range(len(s)):
                if s[i] not in patterndict:
                    patterndict[s[i]] = count
                    count+=1
                    trans.append(count)
                else:
                    trans.append(patterndict[s[i]])
            return ''.join(str(i) for i in trans)

        numbpat=numbify(pattern)
        numbword=[numbify(i) for i in words]
        return [words[index] for index,value in enumerate(numbword) if value in numbpat]
