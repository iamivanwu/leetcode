from typing import List
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        lock = [0]*len(rooms)
        bfs = [0]
        while bfs:
            temp = []
            for room in bfs:
                lock[room] = 1
                for key in rooms[room]:
                    if lock[key] == 0:
                        temp.append(key)
            bfs = temp
        for unlock in lock:
            if not unlock:
                return False
        return True