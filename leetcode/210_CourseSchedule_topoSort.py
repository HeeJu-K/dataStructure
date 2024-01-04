from collections import defaultdict

# have to take all courses

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build mapper 
        # i will be starting from base course to its upper level courses
        courseMap = defaultdict(list)
        for course, prereq in prerequisites:
            courseMap[prereq].append(course)

        # record the indegrees, length of prerequisites
        indegree = [0]*numCourses
        for course, prereq in prerequisites:
            indegree[course] += 1

        # get leaf nodes, we will start from course with no prerequisites
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        # start traversing from base course, find all courses that does not have prereq
        res = []
        while queue:
            prereq = queue.popleft()
            res.append(prereq)
            for course in courseMap[prereq]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)

        # check if there were cycle or not
        # we have to finish all courses thus even one cycle must return []
        hasCycle = len(res) < numCourses
        return [] if hasCycle else res