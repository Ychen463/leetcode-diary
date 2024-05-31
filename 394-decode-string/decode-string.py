class Solution:
    # Method 1: Recursion
    def __init__(self):
        self.index = 0

    def decodeString(self, s: str) -> str:
        # --------------------------------
        # Method 1: Recursion
        result = []
        while self.index < len(s) and s[self.index] != ']':
            # 1. 如果当前字符是字母，直接添加到 result 列表中，并更新索引 index。
            if not s[self.index].isdigit(): # 如果是char 
                result.append(s[self.index])
                self.index +=1
            else:
                # 2. 如果当前字符是digit，构建重复次数 k，处理多位数字。
                k = 0 # 重复次数
                while self.index <len(s) and s[self.index].isdigit():
                    k = k * 10 + int(s[self.index])
                    self.index +=1
                
                # 3. 构造result string “3[a]”
                self.index += 1  # 跳过 '['
                decoded_string = self.decodeString(s)  # 递归处理子字符串
                self.index += 1  # 跳过 ']'
                result.append(decoded_string * k) # 将解码结果重复 k 次并添加到 result 中
        return ''.join(result)

        # --------------------------------
        # Method 2: Stack
        # counter = 0
        # result_st = [] # 用于存储部分结果字符串
        # count_st = [] # 用于存储重复次数
        # cur_string = []

        # for char in s:
        #     if char.isdigit():  # 构建多位数的重复次数
        #         counter = counter * 10 + int(char)
        #     # 如果遇到 [，将当前的部分结果字符串入栈，并开始新的部分结果字符串。
        #     elif char == '[':
        #         result_st.append(cur_string)
        #         count_st.append(counter)
        #         cur_string = []
        #         counter = 0
        #     # 如果遇到 ]，
        #     # 从栈中弹出一个重复次数和一个部分结果字符串，
        #     # 进行解码，并将解码结果附加到部分结果字符串中。
        #     elif char == ']':
        #         cur_count =  count_st.pop()
        #         last_str = result_st.pop()
        #         cur_string =  last_str +  cur_count * cur_string 
        #     else:
        #         cur_string.append(char)
        # return ''.join(cur_string)