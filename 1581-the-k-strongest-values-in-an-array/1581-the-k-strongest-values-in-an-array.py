class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        # get centre of array
        # strongest is whoever have biggest abs difference
        # want k of them
        # idea - take max and min, those r greediest best choice
        # choose whicher to choose from from whichevers best
        # then add to result
        # if equal just choose max
        result = []

        n = len(arr)
        i = int((n-1) / 2)
        arr = sorted(arr)
        middle = arr[i]

        while k > 0:
            mx = abs(arr[-1] - middle)
            mn = abs(arr[0] - middle)

            if mn > mx:
                result.append(arr.pop(0))
            else:
                result.append(arr.pop(-1))
            k -= 1

        return result

