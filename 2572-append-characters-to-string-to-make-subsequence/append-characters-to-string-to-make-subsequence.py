class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        pointer_s = pointer_t = 0
        counter = len(t)
        while pointer_t <len(t) and pointer_s < len(s):
            if t[pointer_t] == s[pointer_s]:
                counter -=1
                pointer_t +=1
            pointer_s +=1

        return counter
        