class Solution:
    def smallestNumber(self, num: int) -> int:
        # return the smallest number rearranged that isnt starting with 0
        # ideal way is to start off using the amsllest number and ending ith largest number
        # s.t. the msb is as small as possible
        # however we want to avoid 0
        # so really
        # if i were to dot his, we get a hashmap and count the frequency of all of the value in nums
        # also store all of the value of nums in a set
        # we get the smallest value (isnt 0) to start off us
        # then we add all of the 0s, then after that we go through each of the smallest values from set
        # and we add that to number by getting the number multiply its frequency in hashmap
        # linear to go through everything ,nlogn to sort array
        # if its negative, we do the complete opposite
        # because really its the same thing except in reverse and we put the smallest value where it belong rather then switching it around
        # or what we could do is make the biggest guy actually
        # so all big numbers then leading 0, if its negative, return that but negative
        # if its not negative, we get smallest value, add it to end, remove wheresmallest value of that was, then reverse it
        num = str(num)
        sign = num[0]
        i = 0
        negative = False
        if not sign.isdigit():
            i += 1
            negative = True 

        count = {}
        numbers = set()

        n = len(num)
        while i < n:
            value = num[i]
            count[value] = count.get(value,0) + 1
            numbers.add(value)
            i += 1

        if "0" in numbers and len(numbers) == 1:
            return 0

        numbers = sorted(list(numbers))[::-1]
        result = ""

        for x in numbers:
            freq = count[x]
            result += (freq * x)

        if negative:
            return (int(result) * -1)
        
        if numbers[-1] != "0":
            result = result[::-1]
            return int(result)
        else:
            second = numbers[-2]
            numberZero = count["0"]

            result = result[:(-1 *(numberZero + 1))]
            result += (numberZero * "0") + second
            result = result[::-1]
            return int(result)
