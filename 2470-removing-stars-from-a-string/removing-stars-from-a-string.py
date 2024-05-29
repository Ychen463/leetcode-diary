import collections
class Solution:
    def removeStars(self, s: str) -> str:

        q = collections.deque()
        for i in range(len(s)):
            if s[i] == "*":
                q.pop()
            else:
                q.append(s[i])
        return ''.join(q)