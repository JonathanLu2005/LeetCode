class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        minimum = float("inf")
        maximum = 0
        mode = 0
        modeVal = 0
        total = 0
        counter = 1
        
        length = sum(count)
        result = (length % 2 == 0)
        if not result:
            median = math.ceil(length / 2)
            medianCount = 1
        else:
            median = length / 2
            medianCount = 2

        medianVal = 0

        for i in range(0, 256):
            num = count[i]

            if num > 0:
                total += (num * i)
                maximum = max(maximum,i)
                minimum = min(minimum,i)

                if num > modeVal:
                    modeVal = num
                    mode = i


                if medianCount > 0 and median >= counter and median < counter + num:
                    if result and median - 1 >= counter and median + 1 < counter + num:
                        medianVal = i * 2
                        medianCount -= 2
                    else:
                        medianVal += i
                        if result:
                            median += 1
                        medianCount -= 1
                counter += num
        mean = total / length
        if result:
            medianVal /= 2
        return [minimum, maximum, mean, medianVal, mode]
                


        



