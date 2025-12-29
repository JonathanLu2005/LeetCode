class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        # for each value store their index and keep going
        # once we hit 3 we do the calculation
        # if theres multiple, we get rid of first one to add new one at end
        # else return -1
        # n to go through everything, but a small bit more to do calculation
        hashmap = {}
        result = float("inf")
        n = len(nums)

        for i in range(0,n):
            x = nums[i]

            if x in hashmap:
                if len(hashmap[x]) == 3:
                    hashmap[x].pop(0)
                    hashmap[x].append(i)
                else:
                    hashmap[x].append(i)
            else:
                hashmap[x] = [i]

            if len(hashmap[x]) == 3:
                arr = hashmap[x]
                f = arr[0]
                s = arr[1]
                l = arr[2]

                res = abs(f-s) + abs(s-l) + abs(l-f)
                result = min(res,result)
        
        if result == float("inf"):
            return -1
        return result