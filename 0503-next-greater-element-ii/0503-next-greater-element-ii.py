class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # for every element in nums, return whats the next greater element
        # else return 0
        # maybe we can do stack?

        # e.g we've 1, and 2 is the next biggest number
        # so we store 2 pop 1
        # we keep 2, we store 1,we keep going, we find 2,whatever
        # and currently we've everything as -1,and then with index 
        # we double the array and index is whatever % length

        nums.extend(nums)
        n = len(nums)

        result = [-1] * int(n/2)

        stack = []

        i = 0

        while i < n:
            value = nums[i]
            index = int(i % (n/2))

            while stack and stack[-1][0] < value:
                v, j = stack.pop(-1)

                if result[j] == -1:
                    result[j] = value

            stack.append([value,index])
            i += 1
        return result

