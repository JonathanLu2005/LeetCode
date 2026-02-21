class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        # string s
        # repeat limit
        # new string using character from s
        # such that no letter appear more than repeat limit in row
        # return largest possible
        # i think
        # 1 => we need largest letter first
        # 2 => alternate letter well to include everything
        # e.g 9 b, 3 a, 3 c
        # bbb aaa bbb ccc bbb
        # ccc bbb aaa bbb
        # length matters
        # balance
        # whats better zzzz zzzaaaaaaaaaaaa
        # so legit the game plan is to focus on THE biggest

        # hashmap => get every letter count
        # heap(?) => sort by biggest letter, we add biggest letter, add 2nd biggest, then put biggest back in, and add whatever
        # until cant anymore

        # c b a, get c from heap add to result, then get b, then if we can add c back in so next time we get c else we get a

        # if its the biggest => add all of it
        # if its the second biggest => add 1 of it
        count = {}

        for x in s:
            count[x] = count.get(x,0) + 1

        result = ""

        letters = sorted(list(count.keys()))
        
        #heap = []

        #for key in count.keys():
        #    heap.append((-ord(key), key))

        #heapq.heapify(heap)

        temporary = None
        while letters:
            #order, letter = heapq.heappop(heap)
            letter = letters.pop(-1)

            if temporary:
                #heapq.heappush(heap, temporary)
                letters.append(temporary)

            #if not temporary or (temporary and order < temporary[0]):
            if not temporary or (letter > temporary):
                add = min(count[letter],repeatLimit)
            else:
                add = 1

            result += (letter * add)
            count[letter] -= add

            if count[letter] > 0:
                #temporary = (order, letter)
                temporary = letter
            else:
                temporary = None

        return result




        