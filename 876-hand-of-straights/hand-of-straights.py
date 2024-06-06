
# # Approach 1: Using Map

# from collections import Counter
# class Solution:
#     def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
#         if len(hand) % groupSize != 0:
#             return False
        
#         card_count = Counter(hand)
#         min_heap = list(card_count.keys())
#         heapq.heapify(min_heap)

#         while min_heap:
#             cur_card = min_heap[0] # get min card
#             for i in range(groupSize):
#                 if card_count[cur_card + i] ==0:
#                     return False
#                 card_count[cur_card+i] -=1
#                  # 减完之后如果= 0我想在min_heap里去掉这个key
#                 if card_count[cur_card + i] ==0:
#                     if cur_card + i != heapq.heappop(min_heap):
#                         return False
#         return True

# ======================================================================

# Approach 2: Rerverse Decrement

from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        card_count = Counter(hand)
        
        for card in hand:
            start_card = card
            while card_count[start_card-1]:
                start_card -= 1
            # 找到start_card
            while  start_card <= card:
                while card_count[start_card]:
                    for i in range(groupSize):
                        if card_count[start_card + i] ==0:
                            return False
                        card_count[start_card + i] -=1
                start_card +=1
        return True
