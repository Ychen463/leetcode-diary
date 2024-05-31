from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        q_r = deque()
        q_d = deque()
        for i , s in enumerate(senate) :
            if s == 'D':
                q_d.append(i)
            else:
                q_r.append(i)
                
        while q_r and q_d:
            Radiant = q_r.popleft()
            Dire = q_d.popleft()
            if Radiant< Dire:
                q_r.append(len(senate) + Radiant)
            else:
                q_d.append(len(senate)+Dire)
        return 'Radiant' if q_r else 'Dire'
                


            
            







#         if "D" not in senate:
#             return "Radiant"
#         if "R" not in senate:
#             return "Dire"
#         while len(senate) > 1:
#             if senate[0] == "R" and "D" in senate[1:]:
# #                 print(senate.index("D"))
#                 senate=senate.replace('D', '', 1)
#                 senate=senate.replace('R', '', 1)
#                 if len(senate) == 0:
#                     return "Radiant"
#             elif senate[0] == "D" and "R" in senate[1:]:
# #                 print(senate.index("D"))
#                 senate=senate.replace('D', '', 1)
#                 senate=senate.replace('R', '', 1)
#                 if len(senate) == 0:
#                     return "Dire"
#         if senate == "D":
#             return "Dire"
#         else:
#             return "Radiant"