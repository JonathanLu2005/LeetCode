class TimeMap:

    def __init__(self):
        self.timestampRecords = {}
        self.keyRecords = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if timestamp not in self.timestampRecords:
            self.timestampRecords[timestamp] = {}

        if key not in self.timestampRecords[timestamp]:
            self.timestampRecords[timestamp][key] = []
        
        self.timestampRecords[timestamp][key].append(value)

        if key not in self.keyRecords:
            self.keyRecords[key] = SortedList()
        self.keyRecords[key].add(timestamp)
        
    def get(self, key: str, timestamp: int) -> str:
        if key in self.keyRecords:
            timestamps = self.keyRecords[key]
        else:
            return ""

        if timestamps[0] > timestamp:
            return ""

        l = 0
        r = len(timestamps) - 1
        target = -1

        while l <= r:
            m = (l+r) // 2

            time = timestamps[m]

            if time < timestamp:
                l = m + 1
            elif time > timestamp:
                r = m - 1
            else:
                target = time
                break

        if target == -1:
            target = timestamps[r]
        
        value = self.timestampRecords[target][key]
        return "".join(value)

# store multiple values for same key at different time stamps
# retrieve key value at certain timestamp
# timestamp -> key -> value
# find most recent time near timestamp for that key, and get the values
# hmmm i reckon i should obv have timestamp -> key -> vlaue
# BUT, i need key -> timestamps
# to easily access tmestamp, to access the above

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)