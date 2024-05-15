"""
greedy
by iterating start to last, we know there exist starting point or not
subdivide the paths into segments
adding paths to cur_gain, if the route fails (cur_gain < 0), look for next starting point
"""
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cur_gain, total_gain = 0, 0
        start = 0

        for i in range (len(gas)):
            total_gain += gas[i] - cost[i]
            cur_gain += gas[i] - cost[i]
            if cur_gain < 0:
                cur_gain = 0
                start = i+1

        return start if total_gain >= 0 else -1