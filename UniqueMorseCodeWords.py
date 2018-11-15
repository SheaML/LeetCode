class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        abc=list(string.ascii_lowercase)
        
        dictionary=dict(zip(abc,morse))
        
        
        translations = []
        
        for w in words:
            
            transl=[]
            for i in w:
                transl.append(dictionary.get(i))
            translations.append(''.join(transl))  

        return len(set(translations))
