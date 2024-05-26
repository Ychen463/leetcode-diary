class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_al = 0
        cur = 0
        for i in range(len(gain)):
            cur +=  gain[i]
            max_al = max(max_al, cur)
        return max_al