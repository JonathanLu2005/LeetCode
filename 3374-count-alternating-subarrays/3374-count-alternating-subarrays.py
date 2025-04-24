class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        # find length of longest alternating subarray
        # then its like n * n - 1 / 2, then add length
        # else if next is same, just add 1
        # 
        result = 0
        length = 0
        current = 2

        for x in nums:
            if x != current:
                length += 1
                current = x
            else:
                result += ((length) * (length - 1)) / 2
                result += length

                length = 1
                current = x

        result += ((length) * (length - 1)) / 2
        result += length
        return int(result)