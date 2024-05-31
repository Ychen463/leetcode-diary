from collections import deque

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
                
        # Method 2: Single Queue
        r_count, d_count = senate.count('R') , senate.count('D')
        floating_ban_r = floating_ban_d = 0
        q = deque(senate)
        while r_count and d_count:
            cur = q.popleft()
            if cur == 'D':
                if floating_ban_r: # D 本轮 被banned
                    floating_ban_r -= 1
                    d_count -=1
                else:
                    floating_ban_d +=1 # 否则 D senator会ban R
                    q.append(cur) # D 行驶ban权利，排队下一轮
            else:
                if floating_ban_d: # D 本轮 被banned
                    floating_ban_d -= 1
                    r_count -=1
                else:
                    floating_ban_r +=1 # 否则 D senator会ban R
                    q.append(cur) # D 行驶ban权利，排队下一轮

        return 'Dire' if d_count else 'Radiant'