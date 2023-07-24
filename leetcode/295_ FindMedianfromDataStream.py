### [-1] operation returns the last element of a heap (for min heap return largest, for max heap return smallest)
### [0] operation returns the first element of a heap (for min heap return smallest, for max heap return largest)

"""
when adding numbers, first add to max heap then add to min heap to ensure the comparison in the whole dataset
have max heap store longer numbers
max heap will store smaller values of large to small order
min heap will store bigger values of small to large order
"""
class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = [] # store negative values

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxheap, -num)
        # item = heapq.heappop(self.maxheap)
        heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))

        if len(self.minheap) > len(self.maxheap):
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))

        # print("check max heap", self.maxheap, "check min heap",self.minheap)
        

    def findMedian(self) -> float:
        if (len(self.minheap)+len(self.maxheap)) % 2: # odd case
            return -self.maxheap[0]
        else:
            return (self.minheap[0] - self.maxheap[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()