class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        # a smarter dp approach, to achieve o n, we can just have hashmap
        # so without needing to go backwards
        # we can use hashmap, if a prev value exist where num - difference exist
        # then we get that + 1 for this value
        # else its 1
        # and continue
        # then get max at end of line
        hashmap = {}

        for num in arr:
            if num-difference in hashmap:
                hashmap[num] = hashmap[num-difference] + 1
            else:
                hashmap[num] = 1

        return max(hashmap.values())
        
        """
        # similar to prev question
        # every time we get to the next num
        # we go backwards and find a value s.t. difference is difference
        # and we get their value (aka chain) and include it to ours
        # if its max
        
        n = len(arr)
        result = [0] * n

        for i in range(0,n):
            c = arr[i]

            res = 0
            for j in range(i-1,-1,-1):
                p = arr[j]

                if c-p == difference:
                    res = max(res,result[j])
                    break

            result[i] += res + 1

        #print(result)

        return max(result)
        """