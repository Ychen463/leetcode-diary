class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        p = 0
        res = ""
        while p <= max(len(word1),len(word2)):
            res+= word1[p]
            res+= word2[p]
            print(res)
            p+=1
            if len(word1)>len(word2) and p == len(word2):
                res+= word1[p:]
                return res
            elif len(word2)>=len(word1) and p == len(word1):
                res+= word2[p:]
                return res
            