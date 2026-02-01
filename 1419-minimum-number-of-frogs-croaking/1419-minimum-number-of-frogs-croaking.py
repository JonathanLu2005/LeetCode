class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        # if its a clean croak, its just 1
        # if its intertwined, we need multiple 
        # ift heres invalid,its -1
        # basically we just need find the most number of intertwined messed up croaks which will determine more frogs
        # maybe we could use a hashmap/bin of some sort?
        # and wej ust holdmax
        # n^2

        # to make it o(n)
        # because all we care about is checking the last letter and if it matches then we add 
        # so we could store that in a hasmhap or an array
        # wait wouldnt work cuz if we had cro cro then we would have o o
        # we could have a counter
        # cro cro ak ak
        # o = 2
        # o = 1, a = 1
        # o = 1, a = 1,
        # hashmap with letter -> counter
        # so O(n)
        # ask urselfwhy we#vexyz, what does it do, and what altnerative can do the samething but faster
        # however might need to manipulate data in a way to allow that to happen
        result = -1

        hashmap = {
            "k": "a",
            "a": "o",
            "o": "r",
            "r": "c"
        }

        counter = {}

        for x in croakOfFrogs:
            if x == "c":
                counter[x] = counter.get(x,0) + 1
            else:
                target = hashmap[x]

                if target in counter and counter[target] != 0:
                    counter[target] -= 1

                    if x != "k":
                        counter[x] = counter.get(x,0) + 1
                    else:
                        # update result byfinding numberof frogs
                        # we can take the sum of all the values so far the counts aka numberfrog + 1
                        current = 1 + sum(counter.values())
                        result = max(result,current)
                else:
                    return -1

        if sum(counter.values()) > 0:
            return -1


        return result
                        
            

                