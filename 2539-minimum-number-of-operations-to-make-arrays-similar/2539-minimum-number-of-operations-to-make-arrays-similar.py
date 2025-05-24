class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        # choose 2 indices, one + 2, another - 2
        # similar if frequency of element are same
        # return min operation to make it similar to target
        # find what needs to be added and subtracted to get close
        # 8: -6 for 2, +2 for 10
        # 12: -2 for 10, +2 for 14
        # 6: -4 for 2, +4 for 10
        # be greedy
        # 6 8 12
        # 2 10 14
        # find differnce from one to another, and use that to figure ot number of operations
        # separate odd and even numbers as only +2, -2, guaranteed answer so fine

        nums = sorted(nums)
        target = sorted(target)

        eNum = []
        oNum = []

        eTarget = []
        oTarget = []

        n = len(nums)

        for i in range(0, n):
            v1 = nums[i]
            v2 = target[i]

            if v1 % 2 == 0:
                eNum.append(v1)
            else:
                oNum.append(v1)

            if v2 % 2 == 0:
                eTarget.append(v2)
            else:
                oTarget.append(v2)

        result = 0

        for v1, v2 in zip(eNum,eTarget):
            result += abs(v1-v2)
        for v1, v2 in zip(oNum,oTarget):
            result += abs(v1-v2)

        result = result / 4
        return int(result)

        