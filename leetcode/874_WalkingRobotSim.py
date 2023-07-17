### finding rules of changing direction
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # heading North: 0,1 || heading South: 0, -1 || heading West: -1, 0 || heading east: 1, 0
        dx, dy = 0, 1 # starting direction is north
        pos_x, pos_y = 0, 0
        obs = {(x, y) for x, y in obstacles} # time complexity O(n)

        max_dis = 0
        for cmd in commands:
            if cmd == -1:
                dy, dx = -dx, dy
            elif cmd == -2:
                dy, dx = dx, -dy
            else: 
                for _ in range (cmd):
                    if (pos_x+dx, pos_y+dy) in obs:
                        break
                    
                    pos_x += dx
                    pos_y += dy
                max_dis = max(pos_x**2 + pos_y**2, max_dis)
        return max_dis