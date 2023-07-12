### d = dict((item[0], []) for item in prerequisites)
### for dictionary, pop and append

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #dictionary of {course: prerequisite}
        d = dict((item[0], []) for item in prerequisites)

        for item in prerequisites:
            d[item[0]].append(item[1])
        print(d)

        visited = []
        def dfs(course):
            if course in visited: # loop detected
                return False
            if not (course in d.keys()) : # has no prerequisite, or course can be taken
                return True
            visited.append(course)
            for pre in d[course]:
                if not dfs(pre): return False # False returned from recursion
            visited.remove(course) # has to be removed as it might be visited from another path
            d.pop(course) # mark as a good node
            return True
        
        for course in range(numCourses): # iterate for disconnected case
            if not dfs(course): return False
        return True

             