class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        pointer_s = pointer_t = 0
        # 遍历s和t，直到其中一个结束
        while pointer_t <len(t) and pointer_s < len(s):
            if t[pointer_t] == s[pointer_s]:
                pointer_t +=1
            pointer_s +=1
        # 返回剩余未匹配的t的字符数量
        return len(t) - pointer_t
        