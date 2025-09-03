class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        # 2d array s.t. only use values in numbers
        # each row have distinct integers
        # just sort array, if same value, create a new array to append to
        # otherwise keep adding to same array
        n = 0
        result = [[]]

        nums = sorted(nums)
        result[n].append(nums[0])

        for i in range(1,len(nums)):
            v = nums[i]
            l = nums[i-1]

            if v == l:
                n += 1

                if n < len(result):
                    result[n].append(v)
                else:
                    result.append([v])
            else:
                n = 0
                result[n].append(v)

        return result
