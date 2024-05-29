import collections
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = collections.deque()

        for asteroid in asteroids:
            # 栈非空且当前小行星向左移动而栈顶小行星向右移动时，发生碰撞:
            while st and asteroid < 0 < st[-1]:
                last_asteroid = st.pop()
                if asteroid == -last_asteroid:
                    break
                elif last_asteroid > -asteroid:
                    st.append(last_asteroid)
                    break
            else:
                st.append(asteroid)
        return list(st)