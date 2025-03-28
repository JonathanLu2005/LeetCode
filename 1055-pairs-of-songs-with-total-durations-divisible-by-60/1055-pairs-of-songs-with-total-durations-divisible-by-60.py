class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # we can store their remainder because thats all we care about!
        # e.g 50 % 60 = 50, so we obviously want something with 10!
        # or 110 and 70
        # mod them by by 60, we get 50 and 10, add both and we get 60
        for i in range(0, len(time)):
            time[i] = time[i] % 60

        # after this its 2 sum 
        hashmap = {}
        result = 0
        time = time[::-1]

        for x in time:
            result += hashmap.get(60-x,0)
            if x == 0:
                result += hashmap.get(x,0)
            hashmap[x] = hashmap.get(x,0) + 1
        return result

