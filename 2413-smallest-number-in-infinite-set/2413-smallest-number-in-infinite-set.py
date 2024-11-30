import heapq
class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        # added_integers 集合实际上是用来记录 "已经被移出主集合的数字（候选集合之外）"
        self.added_integers = set()
        self.current = 1

    def popSmallest(self) -> int:
        if self.heap:
            smallest = heapq.heappop(self.heap)
            self.added_integers.remove(smallest)
        else:
            smallest = self.current
            self.current += 1
        return smallest

    def addBack(self, num: int) -> None:
        if num < self.current and num not in self.added_integers:
            heapq.heappush(self.heap,num)
            self.added_integers.add(num)

        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)