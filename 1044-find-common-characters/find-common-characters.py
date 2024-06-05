from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = Counter(words[0])
        for i in range(1, len(words)):
            word_hm = Counter(words[i])
            for letter in common.keys():
                common[letter] = min(common[letter],word_hm[letter])
        result = []
        for k,v in common.items():
            for _ in range(v):
                result.append(k)
        return result


                

        