class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # store the tempreature and day number 
        # get next tempreature and day number
        # if more then add with number
        n = len(temperatures)
        result = [0] * n
        stack = []

        for i in range(0,n):
            curtemp, curday = temperatures[i], i

            while stack:
                temp, day = stack[-1]

                if curtemp > temp:
                    stack.pop(-1)
                    result[day] = curday-day
                else:
                    break
            stack.append((curtemp,curday))
        return result                    
