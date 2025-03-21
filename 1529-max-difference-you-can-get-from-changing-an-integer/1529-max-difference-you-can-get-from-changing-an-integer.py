class Solution:
    def maxDiff(self, num: int) -> int:
        # small
        # if first isnt 1, we replace that with 1
        # otherwies find first number that isnt 1, replace with 0

        # big
        # if first isnt 9, we replace with 9
        # otherwise find first number that isnt 9 and replace with 9

        num = [str(x) for x in str(num)]

        small = num.copy()
        target = ""
        replace = ""
        found = False
        if small[0] != "1":
            target = small[0]
            replace = "1"
            small[0] = replace
            found = True

        for i in range(1, len(small)):
            if found:
                if small[i] == target:
                    small[i] = replace
            elif small[i] != "1" and small[i] != "0":
                found = True
                target = small[i]
                replace = "0"
                small[i] = replace

        small = int("".join(small))

        big = num.copy()
        found = False
        target = ""

        for i in range(0, len(big)):
            if found:
                if big[i] == target:
                    big[i] = "9"
            elif big[i] != "9":
                found = True
                target = big[i]
                big[i] = "9"
        
        big = int("".join(big))

        return big - small
            
        

        