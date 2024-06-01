class Solution:
    def scoreOfString(self, s: str) -> int:
        abs_sum = 0
        for i in range(1,len(s)):
            abs_sum += abs(ord(s[i-1]) - ord(s[i]))
        return abs_sum