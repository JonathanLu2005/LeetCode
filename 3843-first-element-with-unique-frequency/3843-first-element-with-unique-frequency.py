class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        # what data we need
        # get the frequency of each value
        # amongst the frequencies, find which one isnt repeated
        # and once we have a set of those, find which number appears first s.t. it's the one that isnt repeated
        # after this, wecould iterate through nums and get the counts
        # 1 = [20,10]
        # 2 = [30]
        # then itearte through that again, and moment we get something that is alone, we use that
        count = {}
        for x in nums:
            count[x] = count.get(x,0) + 1

        result = {}
        seen = set()

        for x in nums:
            if x not in seen:
                key = count[x]
                result.setdefault(key,[])
                result[key].append(x)
                seen.add(x)

        for key, value in result.items():
            if len(value) == 1:
                return value[0]
        return -1