import heapq, math

### solution using minheap implemented by heapq (heapq is minheap only)


class ExamRoom:

    def __init__(self, n: int):
        self.n = n
        # intervals is a minheap that stores current available distance in sorted order, starting and ending point. It uses negative distance values to pop the max values
        self.intervals = []
        # initialize min heap with empty seats, it's distance n, starting at -1 and ending at n
        heapq.heappush(self.intervals, (-n, -1, n)) #(dist(negative value), start, end)
        # use dict to store adjacent non-vacant seats, initialize with empty adjacent seats 
        self.adj = {-1: [-2,n], n: [-1, n+1]}
    
        return 

    def seat(self) -> int:
        # in here, intervals is already sorted, pop to get longest interval
        dist, start, end = heapq.heappop(self.intervals)

        if start == -1:
            pos = 0
            if end == self.n:
                dist = self.n-1
            else:
                dist = end//2
            if end-pos == 1:
                heapq.heappush(self.intervals, (0, pos, end ))
            else:
                heapq.heappush(self.intervals, (-dist, pos, end))
        elif end == self.n:
            # in this case, start point is never -1
            pos = self.n-1
            if start == -1:
                dist = pos
            else:
                dist = (pos-start)//2
            if pos-start == 1:
                heapq.heappush(self.intervals, (0, pos, end ))
            else:
                heapq.heappush(self.intervals, (-dist, start, pos))
        else:
            #in this case, longest distance is not at the end
            pos = ((end+start)//2)
            dist = (end - pos)//2
            if end-pos == 1:
                heapq.heappush(self.intervals, (0, pos, end ))
            else:
                heapq.heappush(self.intervals, (-dist, pos, end))
            if pos-start == 1:
                heapq.heappush(self.intervals, (0, pos, end ))
            else:
                heapq.heappush(self.intervals, (math.ceil((start-pos)/2), start, pos))
        self.adj[pos] = [start, end] #store neighbors of pos as start and end
        self.adj[start][1] = pos # update start's right neighbor as pos
        self.adj[end][0] = pos # update end's left neighbor as pos

        return pos
        
    def leave(self, p: int) -> None:
        a, b = self.adj.pop(p) # get left and right neighbors of p, update the neighbors as well
        self.adj[a][1] = b
        self.adj[b][0] = a 

        tmp = []
        
        while self.intervals:
            item = heapq.heappop(self.intervals)
            if item[1] != p and item[2] != p:
                tmp.append(item)
            
        heapq.heapify(tmp)
        self.intervals = tmp
        heapq.heappush(self.intervals, ((a-b)//2, a, b))
        return


if __name__ == '__main__':
# Your ExamRoom object will be instantiated and called as such:
    obj = ExamRoom(8)

    obj.seat()
    obj.seat()
    print("---------------")
    obj.leave(0)
    obj.leave(7)
    print("---------------")
    obj.seat()
    obj.seat()
    obj.seat()
    obj.seat()
    obj.seat()
    obj.seat()
    obj.seat()
    obj.seat()


