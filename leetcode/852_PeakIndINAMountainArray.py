"""
approach: there is only one peak in the array
Find the index of the one maximum value 
Binary Search O(logn)
"""
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        low = 0
        high = n-1
        while low<high:
            mid = low + (high-low)//2
            if arr[mid]<arr[mid+1]:
                low = mid+1
            else:
                high = mid
        return low