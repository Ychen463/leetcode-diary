class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        answer = 0
        position.sort()
        # low 为 1（最小可能距离）。
        # high 为 position[-1] / (m-1)，这是两个极端位置的球之间的最大距离。
        low, high = 1, position[-1] - position[0]
        while low <= high:
            mid = low + (high - low) //2
            if self.canPlaceBall(mid, position, m):
                answer = mid
                low = mid + 1
            else:
                high = mid -1
        return answer



    def canPlaceBall(self, x, position, m):
        prev_ball_pos = position[0]
        balls_placed = 1
        for i in range( 1, len(position)):
            curr_pos = position[i]
            if curr_pos - prev_ball_pos >= x:
                balls_placed +=1
                prev_ball_pos = curr_pos
            if balls_placed == m:
                return True
        return False