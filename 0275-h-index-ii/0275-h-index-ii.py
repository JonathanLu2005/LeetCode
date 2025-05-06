class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # citation i = citation for ith paper
        # h index = max value of h, reseacher published h times and cited h times
        # length = n papers
        # h  = x papers, cited x times
        # opposite? 6 = 1, 5 = 2, 3 = 3
        # so given between value 1-5
        # index it, e.g 3 goes to 3, realise length is 3 so printed at leas
        # and value is 3 so other must be at least 3 or more
        
        # h = h papers with h citations (at least)
        # between 0 to n
        # if m has h papers which have h citations
        # basically if length = citation
        # mapping
        # 0 1 3 5 6
        # 5 4 3 2 1
        # 6 >= 1, 5 >= 2, 3 >= 3 ... 3 is spot
        # go throguh each num and find their h value
        
        n = len(citations)
        l = 0
        r = n - 1
        res = 0

        while l <= r:
            m = (l+r) // 2

            if citations[m] >= n - m:
                res = n - m
                r = m - 1
            else:
                l = m + 1

        return res