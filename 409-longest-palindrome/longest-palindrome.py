from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        freqMap = Counter(s)
        length = 0
        freq_is_odd = False
        for freq in freqMap.values():
            if (freq %2 ==0 ):
                length += freq
            else:
                length += (freq-1)
                freq_is_odd = True
        # 回文字符串的特性是对称的，这意味着每个字符在回文中都应该出现偶数次，
        # 以便能够在中间对称。唯一的例外是回文的中心位置，允许有一个字符出现奇数次，
        # 这个字符可以作为回文的中心。
        if freq_is_odd:
            length += 1
        return length
        
        
        
