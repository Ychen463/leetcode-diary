class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        thres = max(candies) - extraCandies
        res = []
        for each in candies:
            if each >= thres:
                res.append(True)
            else:
                res.append(False)
        return res
