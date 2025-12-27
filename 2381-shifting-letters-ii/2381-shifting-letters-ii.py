class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # 1 is forwards, 0 is backwards
        # from start to end
        # issue is that if we apply it every time probably going to be chaos
        # let say each shift is n and theres m shifts, would be mn
        # so n^2
        # perhaps we can have a bit mask of some sort?
        # where we have array of 0 of n lots
        # then for every points we +1 or -1
        n = len(s)
        array = [0] * (n+1)

        for [start, end, direction] in shifts:
            if direction == 0:
                direction = -1

            array[start] += direction
            array[end+1] -= direction
        
        # get ascii value into 0-25
        # add result on 
        # mod it to get back to 0-25
        # add to regular ascii and bang new result
        result = ""
        current = 0
        for i in range(0,n):
            current += array[i]

            value = ord(s[i]) - 97 + current
            value = value % 26
            value += 97
            result += chr(value)
        return result

