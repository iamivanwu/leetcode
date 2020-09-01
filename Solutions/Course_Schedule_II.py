from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edge = [[]for _ in range(numCourses)]
        study = [0]*numCourses
        path = []
        for a,b in prerequisites:
            edge[a].append(b)
        def run(course):
            if study[course] == -1:
                return False
            if study[course] == 1:
                return True
            study[course] = -1
            for pre in edge[course]:
                if not run(pre):
                    return False
            study[course] = 1
            path.append(course)
            return True
        for course in range(numCourses):
            if not run(course):
                return []
        return path
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(Solution().findOrder(numCourses,prerequisites))