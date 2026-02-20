class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        # num and sum
        # n good if
        # number of digits in n == num
        # sum of digits in n == sum
        # score of n == sum of suqares in n
        # return string result that maximise score
        # have length of num, so that narrows down what numbers we can have
        # and its sum of each digit is the sum
        # that also helps us narrow down the number
        # and for every value from 1 to n, we count the squares
        # so this indicates we want the biggest number possible as it means more squares
        # requirements - biggest number, length of num, add up to sum
        # if not possible return ""
        # algorithm -> we iterate from up to num
        # and from the sum, we try to take 9 away and put it in our result
        # unless the current sum value is < 9, we include that
        # and if its 0 then just add 0 really
        # we keep going until we reach num length and met sum, return result
        # if by the end of num, sum != 0, we return ""
        result = ""

        for i in range(num):
            if sum >= 9:
                result += "9"
                sum -= 9
            else:
                result += str(sum)
                sum -= sum

        if sum > 0:
            return ""
        return result

