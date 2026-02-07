class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        # find subarrays of length k
        # almost unique => at least m distinct values
        # we keep track of subarrays by just having a widnow and sliding it
        # solves the k bit
        # but what about m
        # have at least m distinct elements
        # i think we can have a set that holds all elements we add
        # and as its hold only distinct, we find length of that and if its >= m, we're good
        # HOWEVER
        # to maintain the shifting
        # we should have a hashmap which holds the element and how many time it appeared
        # so if we move to next element and remove the previous one
        # and if the previous one in hashmap we decrement it, and its 0
        # then we remove it from the set, toherwise we keep it as it still exists
        count = {}
        result = 0
        elements = set()
        current = 0
        for i in range(0,k):
            value = nums[i]
            current += value
            elements.add(value)
            count[value] = count.get(value,0) + 1

        n = len(nums)
        j = 0
        for i in range(k,n):
            if len(elements) >= m:
                result = max(current,result)
            
            # remove
            remove = nums[j]
            current -= remove
            count[remove] -= 1
            j += 1
            if count[remove] == 0:
                elements.remove(remove)

            # add
            add = nums[i]
            elements.add(add)
            count[add] = count.get(add,0) + 1
            current += add

        if len(elements) >= m:
            result = max(current,result)
        
        return result