"""
heapify O(n)
Find kth largest: O(klogn)
Add: O(logn)

As I'm tracking the kth largest, I only have to leave k elems in the heap, meaning the n-k elems in the minheap can be popped
"""

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        heapify(nums)
        self.nums = nums
        

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)