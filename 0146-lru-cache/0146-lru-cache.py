class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.hashmap = {}
        self.array = []

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.array.remove(key)
            self.array.insert(0,key)
        return self.hashmap.get(key,-1)

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.hashmap[key] = value
            self.array.remove(key)
            self.array.insert(0,key)
        else:
            if self.size == self.capacity:
                evict = self.array[-1]
                self.array.remove(evict)
                self.hashmap.pop(evict, None)
            else:
                self.size += 1
            self.hashmap[key] = value
            self.array.insert(0,key)
            
# so we have key = value
# and we want to update it 
# and if we try to add and we met the size limit, evict least recently used
# i think, we have hashmap to hold everything
# and then ofc, we have an array of keys
# if we just used it, we remove it and add it to front of array
# such that the end of array = least used key

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)