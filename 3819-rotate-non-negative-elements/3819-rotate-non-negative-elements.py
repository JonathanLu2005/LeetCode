class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        # one idea... is to get all the negatives and their indexes
        # so we could get 1 = -2, 3 = -4
        # and then with our list of negatives e.g -2, -4
        # we shift them
        # then we compare that against the list of indexes, and match
        # o(n) to traverse nums to get all the data
        # to shift... we can do k % length, and only need shift the resulting time
        # by getting last element and adding it to start
        # then o(n) to add it in
        # 3 o(n) operations
        indexes = []
        values = []

        n = len(nums)

        for i in range(0,n):
            value = nums[i]

            if value >= 0:
                values.append(value)
                indexes.append(i)

        if len(values) == 0:
            return nums

        k = k % len(values)

        while k > 0:
            value = values.pop(0)
            values.append(value)
            k -= 1

        m = len(values)
        for i in range(0,m):
            index = indexes[i]
            value = values[i]

            nums[index] = value
        return nums