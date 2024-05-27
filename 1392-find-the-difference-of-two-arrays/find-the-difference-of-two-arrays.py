class Solution:
    # Method 1
    #def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # res = [[],[]]
            # res[0] = list(set([num for num in nums1 if num not in nums2]))
            # res[1] = list(set([num for num in nums2 if num not in nums1]))
            # return res
    
    # Method 2： Hashmap
    def getElementsOnlyInFirstList(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        onlyInNums1 = set()
        existsNums2 = set(nums2)
        for num in nums1:
            if num not in existsNums2:
                onlyInNums1.add(num)
        return list(onlyInNums1)
    def findDifference(self, nums1, nums2):
        return [self.getElementsOnlyInFirstList(nums1, nums2), self.getElementsOnlyInFirstList(nums2, nums1)]
