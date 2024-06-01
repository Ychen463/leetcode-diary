from collections import deque
from bisect import bisect_left
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # # Method 1: 2 Queue 
        # q_r = deque()
        # q_d = deque()

        # # 初始化队列，存储每个参议员的索引
        # for i, s in enumerate(senate):
        #     if s == 'R':
        #         q_r.append(i)
        #     else:
        #         q_d.append(i)

        # # 模拟投票过程
        # n = len(senate)
        # while q_r and q_d:
        #     r_index = q_r.popleft()  # 弹出Radiant参议员的索引
        #     d_index = q_d.popleft()  # 弹出Dire参议员的索引

        #     if r_index < d_index:
        #         # 如果R的索引小，R胜出，R重新排队，索引加n
        #         q_r.append(r_index + n)
        #     else:
        #         # 如果D的索引小，D胜出，D重新排队，索引加n
        #         q_d.append(d_index + n)

        # # 判断最终胜利者
        # return "Radiant" if q_r else "Dire"
                
        # # Method 2: Single Queue
        # r_count, d_count = senate.count('R') , senate.count('D')
        # floating_ban_r = floating_ban_d = 0
        # q = deque(senate)
        # while r_count and d_count:
        #     cur = q.popleft()
        #     if cur == 'D':
        #         if floating_ban_r: # D 本轮 被banned
        #             floating_ban_r -= 1
        #             d_count -=1
        #         else:
        #             floating_ban_d +=1 # 否则 D senator会ban R
        #             q.append(cur) # D 行驶ban权利，排队下一轮
        #     else:
        #         if floating_ban_d: # D 本轮 被banned
        #             floating_ban_d -= 1
        #             r_count -=1
        #         else:
        #             floating_ban_r +=1 # 否则 D senator会ban R
        #             q.append(cur) # D 行驶ban权利，排队下一轮

        # return 'Dire' if d_count else 'Radiant'

        # # Method 3 Greedy Algorithm
        # senate = list(senate) # 换成list因为可以进行删减
        # d_count = senate.count('D')
        # r_count = len(senate) - d_count
        
        # # 定义禁令函数，从指定位置开始寻找并禁止对方参议员
        # def ban(to_ban, start_index):
        #     # loop_around的作用是在每次指针移动时检查是否回到了列表的开头。
        #     # 如果指针已经回到了列表的开头，说明我们已经遍历了一轮。
        #     # 这样做是为了确保我们能够正确地找到并禁掉一个对方参议员。
        #     loop_around = False 
        #     pointer = start_index
        #     while True: # 用while是为了找到 start_index后的 第一个看到的敌人
        #         if pointer == 0:
        #             loop_around = True
        #         if senate[pointer] == to_ban:
        #             senate.pop(pointer)
        #             break
        #         pointer = (pointer+1)% len(senate)
        #     return loop_around

        # turn = 0
        # while d_count and r_count:
        #     # ban_senator_before 的意思是刚好轮换了一轮
        #     if senate[turn] == 'D':
        #         ban_senator_before = ban('R', (turn + 1 ) % len(senate))
        #         r_count -= 1
        #     elif senate[turn] == 'R':
        #         ban_senator_before = ban('D', (turn + 1 ) % len(senate))
        #         d_count -= 1
        #     if ban_senator_before:
        #         turn -= 1
        #     turn = (turn+1) % len(senate)
        # return 'Dire' if d_count else 'Radiant'

        # # Method 4 Boolean Array
        # d_count, r_count = senate.count('D'),senate.count('R')
        # banned = [False] * len(senate)


        # def ban(to_ban, start_with):
        #     pointer = start_with
        #     while True:
        #         if senate[pointer] == to_ban and not banned[pointer]:
        #             banned[pointer] = True
        #             break
        #         pointer = (pointer +1 ) % len(senate)
        
        # turn = 0
        # while d_count and r_count:
        #     if not banned[turn]:
        #         if senate[turn] == 'D':
        #             ban('R', (turn+1) %len(senate))
        #             r_count -=1
        #         else :
        #             ban('D', (turn+1) %len(senate))
        #             d_count -=1
        #     turn = (turn+1) % len(senate)
        # return 'Dire' if d_count else 'Radiant'

        # Method 5 Binary Search
        banned = [False] * len(senate)
        r_indices = [ i for i in range(len(senate)) if senate[i] == 'R']
        d_indices = [ i for i in range(len(senate)) if senate[i] == 'D']

        # 禁止从start_at位置开始的indices_array中的下一个参议员
        def ban(indices_array, start_with):
            # 使用二分查找找到下一个要禁止的参议员的索引
            temp = bisect_left(indices_array,start_with)
             # 如果start_at大于最后一个索引，从头开始查找并禁止第一个参议员
            if temp == len(indices_array):
                banned[indices_array.pop(0)] = True
            else:
                banned[indices_array.pop(temp)] = True

        turn = 0
        while r_indices and d_indices:
            if not banned[turn]:
                if senate[turn] == 'D' :
                    ban(r_indices, turn)
                else:
                    ban(d_indices, turn)
            turn = (turn+1) % len(senate)
        # 当其中一个党派的参议员列表为空时，返回另一个党派为胜利者。
        return 'Radiant' if not d_indices else 'Dire'