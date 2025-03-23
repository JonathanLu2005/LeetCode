class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        # string of colour
        # A B
        # alice then bob
        # remove A iff neighbours are A
        # vice versa for B
        # cant remove peices from edge of line
        # if player cant make turn, then lose
        # return true if alice win vice versa

        # sliding window, count A that are together
        # then B, if >= 3, -2
        # whoever has more is the winner
        acount = 0
        bcount = 0

        colors += "c"

        current = colors[0]
        count = 1

        for i in range(1, len(colors)):
            if current == colors[i]:
                count += 1
            else:
                if count >= 3:
                    count -= 2
                    if current == "A":
                        acount += count
                    else:
                        bcount += count
                current = colors[i]
                count = 1
        
        return (acount > bcount)