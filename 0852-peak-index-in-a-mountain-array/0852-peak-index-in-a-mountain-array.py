class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # isnt it just increase icnrease increase decrease
        # so moment to goes from increase to decrease
        for i in range(1,len(arr) - 1):
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                return i