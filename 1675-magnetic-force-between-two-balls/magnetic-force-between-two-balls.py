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
                low = mid + 1 # 如果可以，试图增加距离
            else:
                high = mid -1
        return answer

    def canPlaceBall(self, x, position, m):
        #这个函数用于检查在给定距离 x 下是否可以放置 m 个球。

        prev_ball_pos = position[0] #初始放置第一个球在 position[0]。
        balls_placed = 1
        for i in range( 1, len(position)):
            curr_pos = position[i]
            # 遍历数组，如果当前位置与上一个放置球的位置之间的距离大于等于 x，
            # 则放置一个球，并更新上一个球的位置。
            if curr_pos - prev_ball_pos >= x:
                balls_placed +=1
                prev_ball_pos = curr_pos
            if balls_placed == m:
                return True
        return False