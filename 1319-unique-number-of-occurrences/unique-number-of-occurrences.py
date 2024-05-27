# import collections
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # counter = Counter(arr)
        # return len(counter.values()) == len(set(counter.values()))
        
        # Method 2: hashMap
        hashMap = {}
        for num in arr:
            hashMap[num]=hashMap.get(num,0) +1
        return len(hashMap) == len(set(hashMap.values()))
