# import collections
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # counter = Counter(arr)
        # return len(counter.values()) == len(set(counter.values()))
        
        # Method 2: hashMap
        hashMap = {}
        for num in arr:
            if num not in hashMap:
                hashMap[num] = 1
            else:
                hashMap[num] += 1
        
        return len(hashMap) == len(set(hashMap.values()))

        # occurances = [each for each in hashMap.values]
        # return len(set(hashMap.values)) == len(hashMap.values)