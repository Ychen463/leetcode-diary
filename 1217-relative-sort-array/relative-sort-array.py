import collections
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dict1 = Counter(arr1)
        res = []
        for num in arr2:
            if num in dict1:
                for i in range(dict1[num]):
                    res.append(num)
        res2 = sorted([ num for num in arr1 if num not in arr2])
        return res+ res2
