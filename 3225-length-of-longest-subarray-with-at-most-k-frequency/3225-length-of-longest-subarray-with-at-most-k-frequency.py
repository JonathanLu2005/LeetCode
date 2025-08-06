class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        # good subarray = all elements frequency are <= k
        # so as we construct widnow, we increment count of each value
        # moment we hit > k, we stop
        # and save result
        # then keep decrementing values till value we've is < k
        length = 0
        result = 0
        hashmap = {}
        i = 0

        for x in nums:
            hashmap[x] = hashmap.get(x,0) + 1

            if hashmap[x] > k:
                result = max(result,length)

                while hashmap[x] > k:
                    value = nums[i]
                    hashmap[value] -= 1
                    length -= 1
                    i += 1
            
            length += 1

        return max(length,result)
