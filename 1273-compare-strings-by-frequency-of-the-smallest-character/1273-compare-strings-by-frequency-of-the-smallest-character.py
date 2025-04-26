class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        # have words and queries
        # for each query, count number of words where queries < words
        # return answer where i is ith query answer

        # query < words, count how many this exist = answer for i
        wordCount = []
        queryCount = []

        for word in words:
            wordCount.append(word.count(min(word)))

        for query in queries:
            queryCount.append(query.count(min(query)))

        wordCount = sorted(wordCount)

        answer = []

        for query in queryCount:
            l = 0
            r = len(wordCount) - 1

            while l <= r:
                m = (l+r) // 2

                if wordCount[m] > query:
                    r = m - 1
                else:
                    l = m + 1

            answer.append(len(wordCount) - l)
        return answer


        