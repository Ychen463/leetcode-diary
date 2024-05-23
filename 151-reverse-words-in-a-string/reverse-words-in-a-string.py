class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = s.strip().split()
        return " ".join(s_list[::-1])
        