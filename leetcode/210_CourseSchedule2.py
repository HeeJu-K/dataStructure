class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        dict = {i: [] for i in range (numCourses)} # dict {course: prerequisite}
        for course, prereq in prerequisites:
            dict[course].append(prereq)
        # dictionary is made

        result = []
        visited = set()

        def dfs(cur):
            if cur in visited:
                return False
            if dict[cur] == []:
                if cur not in result: result.append(cur)
                return True
            visited.add(cur)
            for pre in dict[cur]:
                if not dfs(pre): return False
            result.append(cur)
            visited.remove(cur)
            dict[cur] = []
            return True

        for i in range (numCourses):
            if not dfs(i):
                return []
        
        return result