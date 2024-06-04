# # Method 1: Greedy Way (Hash Table)
# from collections import Counter
# class Solution:
#     def longestPalindrome(self, s: str) -> int:
#         freqMap = Counter(s)
#         length = 0
#         freq_is_odd = False
#         for freq in freqMap.values():
#             if (freq %2 ==0 ):
#                 length += freq
#             else:
#                 length += (freq-1)
#                 freq_is_odd = True
#         # 回文字符串的特性是对称的，这意味着每个字符在回文中都应该出现偶数次，
#         # 以便能够在中间对称。唯一的例外是回文的中心位置，允许有一个字符出现奇数次，
#         # 这个字符可以作为回文的中心。
#         if freq_is_odd:
#             length += 1
#         return length
# ------------------------------------------------------------------

# Method 2: Greedy Way (Optimized)
from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        freqMap = {}
        odd_freq_count = 0
        for char in s:
            freqMap[char] = freqMap.get(char, 0) + 1
            if (freqMap[char] % 2) != 0:
                odd_freq_count +=1 
            else:
                odd_freq_count -=1

        if odd_freq_count >0:
            return len(s) - odd_freq_count+1
        else:
            return len(s)


        
        
