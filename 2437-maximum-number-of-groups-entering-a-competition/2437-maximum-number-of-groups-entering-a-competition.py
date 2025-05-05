class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        #ith group < sum of i+1 group
        # num students ith group < i+1th group
        # will be 1 2 3 so on
        # could sort and do min?
        # so 3 5 6 7 10 12
        # 3
        # 5 6
        # 7 10 12
        # 
        grades = sorted(grades)

        res = 0
        groupSize = 1
        maxSum = 0

        while grades:
            newGroup = 0
            count = 0

            while count < groupSize:
                if grades:
                    newGroup += grades[0]
                    grades.pop(0)
                    count += 1
                else:
                    break
            #print(count)
            #print(newGroup)
            #print(maxSum)
            if count == groupSize and newGroup > maxSum:
                res += 1
                groupSize += 1
                maxSum = newGroup
            else:
                break

        return res
        