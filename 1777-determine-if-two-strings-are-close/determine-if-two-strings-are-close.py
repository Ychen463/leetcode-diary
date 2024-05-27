import collections
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        hp1 = collections.Counter(word1)
        hp2 = collections.Counter(word2)

        # 为了判断两个字符串是否接近，我们需要满足以下几个条件：
        # 1. 两个字符串的长度必须相同。
        # 2. 两个字符串包含的字符集合必须相同。
        # 3. 每个字符出现的频率必须相同（可以通过重排字符来实现频率匹配）。
            # 例如： 
            #  hp1 = {'c': 1, 'a': 2, 'b': 3} 
            # hp2 = {'a': 1, 'b': 2, 'c': 3}
        if len(word1) != len(word2) or set(hp1.keys()) != set(hp2.keys()) or sorted(hp1.values()) != sorted(hp2.values()):
            return False
        return True
