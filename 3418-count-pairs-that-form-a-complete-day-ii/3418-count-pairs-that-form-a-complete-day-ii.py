class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        for i, hour in enumerate(hours):
            hours[i] = hour % 24

        hours = hours[::-1]
        hashmap = {}
        count = 0

        for hour in hours:
            count += hashmap.get(24 - hour, 0)
            if hour == 0:
                count += hashmap.get(hour,0)
            hashmap[hour] = hashmap.get(hour,0) + 1
        return count