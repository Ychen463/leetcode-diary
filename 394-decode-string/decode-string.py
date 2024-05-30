class Solution:
    def decodeString(self, s: str) -> str:
        count_st = []
        counter = 0
        result_st = []
        cur_str = []
        for char in s:
            if char.isdigit():
                counter = counter * 10 + int(char)
            elif char == '[':
                count_st.append(counter)
                result_st.append(cur_str)
                counter = 0
                cur_str = []
            elif char == ']':
                cur_count = count_st.pop()
                last_str = result_st.pop()
                cur_str = last_str + cur_count * cur_str
            else:
                cur_str.append(char)
        return ''.join(cur_str)









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