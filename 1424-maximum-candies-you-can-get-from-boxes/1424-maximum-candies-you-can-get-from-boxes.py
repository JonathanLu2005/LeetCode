class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        # 0 to n-1 boxes
        # status ith box = 1 if open, 0 if closed
        # candies ith box = num candies
        # keys ith box = labels of box can open after ith box
        # contained box ith box = boxes inside ith box

        # initialb xoes - label of box have, take candy from open box, use key to open new box, use box find in it
        # return max candies following rule above

        # bfs ??? use intiial boxwes as a queue, add all other boxes
        # if open box if its open - get contained boxes, and continue
        # and just get the candies and whatnot

        # if box is closed, will need to get a key, which can get from box

        result = 0
        closed = set()
        gotKeys = set()

        while initialBoxes:
            # get box
            b = initialBoxes.pop(0)

            # if open
            if status[b] == 1:
                # add other boxes
                initialBoxes.extend(containedBoxes[b])

                # for any key, if got key for clsoed box can use
                for key in keys[b]:
                    if key in closed:
                        initialBoxes.append(key)
                        #status[key] = 1
                        closed.remove(key)
                    # otherwise just add it to keys to refer to
                    else:
                        gotKeys.add(key)
                    status[key] = 1
                result += candies[b]
            else:
                # else if closed check if has key
                if b in gotKeys:
                    gotKeys.remove(b)
                    initialBoxes.append(b)
                # else add to closed
                else:
                    closed.add(b)
        return result