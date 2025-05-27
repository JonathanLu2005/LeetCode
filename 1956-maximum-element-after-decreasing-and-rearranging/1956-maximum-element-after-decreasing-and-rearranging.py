class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        # perform operations so the array is this
        # first element = 1
        # difference between 2 adjacent element <= 1
        # 2 operations, decrease value of any element arr
        # or rearrange to be in any order
        # return max elemnt toa chieve this

        # sort first 
        # tehn able tell which one needs to be decreased because difference will be way toooo high

        arr = sorted(arr)

        # make sure first is 1 so decrease
        if arr[0] != 1:
            arr[0] = 1

        n = len(arr)

        for i in range(1,n):
            v1 = arr[i-1]
            v2 = arr[i]

            if abs(v1-v2) > 1:
                # minise decrease
                arr[i] = v1 + 1

        return max(arr)