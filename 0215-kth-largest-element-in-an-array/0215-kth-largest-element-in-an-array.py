class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        print(sorted(nums))
        return sorted((nums))[-k]
        