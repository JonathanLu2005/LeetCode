class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        # 0 is empty, 1 is security
        # laser beam between 2 devices iff on different rows and for rows between no others in way
        # basically find number of beams on each level
        # e.g 3 -> 0 -> 2 -> 1
        # so it'll be 3 * 2 + 2 * 1
        count = 0
        prev = -1
        result = 0

        for device in bank:
            for c in device:
                if c == "1":
                    count += 1

            if count > 0:
                if prev == -1:
                    prev = count
                else:
                    result += (count * prev)
                    prev = count
                count = 0
        
        return result