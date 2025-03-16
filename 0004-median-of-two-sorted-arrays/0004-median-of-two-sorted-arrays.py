class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = sorted(nums1 + nums2)

        length = len(arr) 

        if length % 2 == 1:
            return arr[length // 2]
        else:
            val1 = length // 2
            val2 = val1 - 1

            return (arr[val1] + arr[val2]) / 2
