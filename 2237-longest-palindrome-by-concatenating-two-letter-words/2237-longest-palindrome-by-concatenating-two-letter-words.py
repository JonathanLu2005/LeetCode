class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        # 2 cases, if we've letters like xx, its fine we can add it in if the numbers are right
        # e.g cc aa wont work but cc aa cc will
        # other case is xy, need find yx, these will always work can always add it randomly
        # so in a string we can only have 1 odd number of xx, rest must be even

        even = {}
        odd = {}

        result = 0

        # can already add the xy in if possible, else store evens
        for word in words:
            # odds
            if word[0] != word[1]:
                rev = word[1] + word[0]

                if odd.get(rev,0) > 0:
                    odd[rev] -= 1
                    result += 4
                else:
                    odd[word] = odd.get(word,0) + 1
            else:
                even[word] = even.get(word,0) + 1

        maxHeap = []

        # put even to heap make life easy
        for key, value in even.items():
            heapq.heappush(maxHeap, (-value, key))

        oddseen = False
        while maxHeap:
            value, key = heapq.heappop(maxHeap)
            value *= -1

            if value % 2 == 1:
                if not oddseen:
                    oddseen = True

                    result += value * 2
                else:
                    result += (value-1) * 2
            else:
                result += (value) * 2

        return result