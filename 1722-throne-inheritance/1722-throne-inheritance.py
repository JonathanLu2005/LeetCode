class ThroneInheritance:

    def __init__(self, kingName: str):
        self.hashmap = {}

        self.king = kingName

        self.hashmap[kingName] = []

        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        if parentName in self.hashmap:
            self.hashmap[parentName].append(childName)
        else:
            self.hashmap[parentName] = [childName]

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        # it is dfs... we go through 1 branch
        # and keep getting them
        # from left to right 
        result = []

        stack = [self.king]

        while stack:
            node = stack.pop(0)

            if node:
                if node not in self.dead:
                    result.append(node)

                if node in self.hashmap:
                    stack = self.hashmap[node] + stack

        return result

    
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

# idea is that we have many hashmaps
# so king = andy, bob, catherine
# andy = matthew
# bob = alex, asha
# then we go through king, and get the other people
# so access andy to find whoever
# however, we can have a data structure to hold the dead!
# and get rid of them