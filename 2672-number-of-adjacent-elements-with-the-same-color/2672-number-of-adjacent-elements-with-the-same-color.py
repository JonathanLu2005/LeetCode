class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        # have array n
        # set to 0
        # have query which change the index to a new colour
        # count number pairs with same colour
        # maybe keep track if they got same colour over time
        # so we make array of n
        # make hashmap of every index possible
        # set to false ofc
        # then evreytime we update, set to true or whatever
        # and everytime we've to check
        # we take length of true

        # instead of checking everytime it change
        # we just check when we change
        # then we get last result, + - it depedning if we went from true to false or not
        # f match but it was false, then we care
        # if not match but was true, then we care
        result = [0]
        array = [0] * n
        hashmap = {}

        if n == 1:
            return [0] * len(queries)

        for i in range(0,n-1):
            hashmap[(i,i+1)] = False

        index, colour = queries.pop(0)
        array[index] = colour
        

        for [index, colour] in queries:
            array[index] = colour
            total = 0

            if index == 0:
                if array[index] == array[index+1] and hashmap[(index,index+1)] == False:
                    hashmap[(index,index+1)] = True
                    total += 1
                elif array[index] != array[index+1] and hashmap[(index,index+1)] == True:
                    hashmap[(index,index+1)] = False
                    total -= 1
            elif index == n-1:
                if array[index] == array[index-1] and hashmap[(index-1,index)] == False:
                    hashmap[(index-1,index)] = True
                    total += 1
                elif array[index] != array[index-1] and hashmap[(index-1,index)] == True:
                    hashmap[(index-1,index)] = False
                    total -= 1
            else:
                if array[index] == array[index+1] and hashmap[(index,index+1)] == False:
                    hashmap[(index,index+1)] = True
                    total += 1
                elif array[index] != array[index+1] and hashmap[(index,index+1)] == True:
                    hashmap[(index,index+1)] = False
                    total -= 1

                if array[index] == array[index-1] and hashmap[(index-1,index)] == False:
                    hashmap[(index-1,index)] = True
                    total += 1
                elif array[index] != array[index-1] and hashmap[(index-1,index)] == True:
                    hashmap[(index-1,index)] = False
                    total -= 1
            result.append(result[-1] + total)

        return result
