class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = second = float("inf")
        for i in range(len(nums)):
            if nums[i] < first:
                first = nums[i]
            elif nums[i] < second and nums[i] > first:
                second = nums[i]
            elif nums[i] > first and nums[i] > second:
                return True
        return False

        