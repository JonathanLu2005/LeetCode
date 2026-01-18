class Solution:
    def search(self, nums: List[int], target: int) -> int:
        p1 = 0
        p2 = len(nums) - 1

        while p1 <= p2:
            mid = int((p1+p2) / 2)
            val = nums[mid]

            if val == target:
                return mid
            elif val < target:
                p1 = mid + 1
            else:
                p2 = mid - 1
        return -1