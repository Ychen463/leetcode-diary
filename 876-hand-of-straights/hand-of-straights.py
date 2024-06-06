from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        card_count = Counter(hand)
        min_heap = list(card_count.keys())
        heapq.heapify(min_heap)

        while min_heap:
            cur_card = min_heap[0] # get min card
            for i in range(groupSize):
                if card_count[cur_card + i] ==0:
                    return False
                card_count[cur_card+i] -=1
                 # 减完之后如果= 0我想在min_heap里去掉这个key
                if card_count[cur_card + i] ==0:
                    if cur_card + i != heapq.heappop(min_heap):
                        return False
        return True

            
