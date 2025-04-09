class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        # amount that are common in term of numbers shared

        # as we traverse both, we have a set
        # its legit how many we share
        # need a way to intersect the sets together and see length and we append that
        aSet = set()
        bSet = set()
        c = []

        for i in range(0, len(A)):
            aSet.add(A[i])
            bSet.add(B[i])

            cSet = aSet.intersection(bSet)
            c.append(len(cSet))

        return c
        