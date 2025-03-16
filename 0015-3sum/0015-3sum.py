class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # dont reuse same value twice
            if i > 0 and a == nums[i-1]:
                continue

            # pointers
            l, r = i + 1, len(nums) - 1

            # stop once pass
            while l < r:
                # what we're trying to achieve
                threeSum = a + nums[l] + nums[r]

                # adjust pointers
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    # add to res then change l till its new
                    # then keep going to see if we cna do achieve the result with same a and new pointers
                    res.append([a, nums[l], nums[r]])
                    l += 1

                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return res



                













        """
        # tell ourselves we already done all combos that begins with a x value
        # so thats like our key
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threesome = a + nums[l] + nums[r]
                if threesome > 0:
                    r -= 1
                elif threesome < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    # update left pointer till its different, as know
                    # if move -2 to -2 to -2, already found sol
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return res
        """

"""
        finalArr = []
        temp = []

        for i, n in enumerate(nums):
            target = -n
            temp = nums
            temp.pop(i)
            temp.sort()
            arr = []

            left = 0
            right = len(temp) - 1

            while left < right:
                if temp[left] + temp[right] == target:
                    arr = [temp[left], temp[right], n]
                    arr.sort()
                    if arr not in finalArr:
                        finalArr.append(arr)
                elif temp[left] + temp[right] < target:
                    left += 1
                else:
                    right -= 1
            
        return finalArr
"""
"""
        finalArr = []
        for i, n in enumerate(nums):
            prevMap = {} 
            val = n
            arr = []

            for j, m in enumerate(nums):
                if j == i:
                    pass
                else:
                    if -(n + m) in prevMap:
                        arr = [m, -(n+m)]
                    else:
                        prevMap[m] = j
            arr.append(n)
            print(arr)
            arr.sort()
            if arr not in finalArr and len(arr) == 3:
                finalArr.append(arr)

        return finalArr
"""