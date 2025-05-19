class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        # og text is in top left to bottom right
        # get each slanted one
        # then get it in rows
        # if whole row blank just stop

        # ned create grid first, have x rows, no idea abt columns
        # get length of string / rows get column
        n = len(encodedText)
        columns = int(n / rows)
        grid = [[" " for _ in range(columns)] for _ in range(rows)]
        
        r = 0
        c = 0
        for x in encodedText:
            grid[r][c] = x

            c += 1
            if c == columns:
                c = 0
                r += 1
        
        text = ""
        # rows = 4
        # for 0 0, 1 1, 2 2, 3 3
        # 0 1, 1 2, 2 3, so keep adding 11 from 0 to number of columns
        # if word is just purely blank no point
        for c in range(0, columns):
            word = ""
            r = 0
            l = " " * (columns-c)
            
            for x in range(rows):
                if r < rows and c < columns:
                    word += grid[r][c]
                    r += 1
                    c += 1
                else:
                    break

            if word == l:
                break
            text += word

        return text.rstrip()

            