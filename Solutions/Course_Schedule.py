from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[]for _ in range(numCourses)]
        can = [0]*numCourses
        for pre in prerequisites:
            graph[pre[0]].append(pre[1])
        def run(course):
            if can[course] == -1:
                return False
            if can[course] == 1:
                return True
            can[course] = -1
            for c in graph[course]:
                if not run(c):
                    return False
            can[course] = 1
            return True
        for i in range(numCourses):
            if not run(i):
                return False
        return True
numCourses = 2
prerequisites = [[1,0],[0,1]]
numCourses = 3
prerequisites = [[2,1],[1,0]]
numCourses = 3
prerequisites = [[1,0],[0,2],[2,1]]
print(Solution().canFinish(numCourses,prerequisites))