import heapq
class SmallestInfiniteSet:
    def __init__(self):
        self.heap = []
        self.removed = set()
        self.current = 1

    def popSmallest(self) -> int:
        if self.heap:
            smallest = heapq.heappop(self.heap)
            self.removed.remove(smallest)
            return smallest
        smallest = self.current
        self.current += 1
        return smallest
        

    def addBack(self, num: int) -> None:
        if num < self.current and num not in self.removed:
            heapq.heappush(self.heap,num)
            self.removed.add(num)




# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)