class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:
        # a b pos, a <= b
        # x = a^3 + b^3
        hashmap = {}
        result = []

        for i in range(1,int((n ** (1/3)))+1):
            for j in range(1,i+1):
                value = (i**3) + (j**3)

                if value <= n:
                    hashmap[value] = hashmap.get(value,0) + 1

                    if hashmap[value] == 2:
                        result.append(value)
                else:
                    break

        return sorted(result)