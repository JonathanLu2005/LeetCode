class Solution:
    def prefixConnected(self, words: List[str], k: int) -> int:
        # prefix connected if prefix matches from 0 to k-1
        # return groups which has least 2 words
        # could do hashmap, and increment the prefix and groups, and store that, and for every guy thats more then 2
        # chill
        count = {}
        result = set()

        for word in words:
            if len(word) >= k:
                prefix = word[0:k]
                count[prefix] = count.get(prefix,0) + 1

                if count[prefix] >= 2:
                    result.add(prefix)
        return len(result)