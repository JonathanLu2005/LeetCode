class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # tree produce different fruit
        # 2 basket = hold only single type of fruit
        # return max fruit
        # sliding window?
        # moment we hit a new kind of fruit
        # we only keep the previous one, rest are discarded
        result = 0
        b1 = -1
        b2 = -1
        t1 = 0
        t2 = 0
        l = 0
        n = len(fruits)
        hashmap = {}

        for i in range(0,n):
            x = fruits[i]
            # starting off
            if b1 == -1:
                if x != b2:
                    b1 = x
            elif b2 == -1:
                if x != b1:
                    b2 = x

            # but what if neither
            # store fruit at index s.t. able tell when last appeared
            if (b1 != x and b2 != x):
                result = max(result, t1+t2)
                prev = fruits[i-1]

                if prev == b1:
                    target = b2
                else:
                    target = b1

                last = hashmap[target]
                newAmount = (i-1) - last

                b1 = prev
                t1 = newAmount
                b2 = x
                t2 = 0

                



            # increment
            if b1 == x:
                t1 += 1
            if b2 == x:
                t2 += 1
            hashmap[x] = i

        return max(result,t1+t2)

            