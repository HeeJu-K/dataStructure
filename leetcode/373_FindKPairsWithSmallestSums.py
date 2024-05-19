import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        min_heap = [(nums1[0]+nums2[0], 0,0)]
        visited = set((0,0))
        res = []
        
        while k>0 and min_heap:
            _, m1, m2 = heapq.heappop(min_heap)
            res.append((nums1[m1], nums2[m2]))
            if (m1+1<len(nums1)) and (m1+1, m2) not in visited:
                heapq.heappush(min_heap, (nums1[m1+1]+nums2[m2], m1+1, m2))
                visited.add((m1+1, m2))
            if (m2+1<len(nums2)) and (m1, m2+1) not in visited:
                heapq.heappush(min_heap, (nums1[m1]+nums2[m2+1], m1, m2+1))
                visited.add((m1, m2+1))
            k -= 1
            
        return res