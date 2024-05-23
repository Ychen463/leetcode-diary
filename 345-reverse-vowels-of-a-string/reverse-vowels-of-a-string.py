class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a','e','i','o','u',"A","E","I","O","U"]
        s_list = list(s)
        p1, p2 = 0, len(s)-1
        
        while p1 < p2:
            # 找到左边的第一个元音字符
            while p1 < p2 and s_list[p1] not in vowels:
                p1 +=1
            # 找到右边的第一个元音字符
            while p1 < p2 and s_list[p2] not in vowels:
                p2 -=1
            # 交换两个元音字符
            if p1 < p2:
                s_list[p1], s_list[p2] = s_list[p2], s_list[p1]
                p1 += 1
                p2 -= 1
        return "".join(s_list)

        

        
