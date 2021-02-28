from typing import List
class ThroneInheritance:
    def __init__(self, kingName: str):
        self.inhertArr = []
        self.deaths = {}
        self.table = {}

    def birth(self, parentName: str, childName: str) -> None:
        if not self.table.get(parentName):
            self.table[parentName] = [childName]
        else:
            self.table[parentName].append(childName)

    def death(self, name: str) -> None:
        self.deaths[name] = True

    def getInheritanceOrder(self) -> List[str]:
        self.inhertArr = []
        self.getChildren('king')
        return self.inhertArr
    
    def getChildren(self, name):
        if not self.deaths.get(name):
            self.inhertArr.append(name)
        if self.table.get(name):
            for child in self.table[name]:
                self.getChildren(child)

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()