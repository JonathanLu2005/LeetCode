class TrieNode():
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for x in word:
            if x not in cur.children:
                cur.children[x] = TrieNode()
            cur.children[x].count += 1
            cur = cur.children[x]

    def search(self, word: str) -> int:
        result = 0

        cur = self.root

        for x in word:
            result += cur.children[x].count
            cur = cur.children[x]
        
        return result


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        # convert to trie and for every character have count of how many time it appears
        # such that we can search for the word eg abc, and able count for a, ab, abc

        trie = Trie()

        for word in words:
            trie.insert(word)

        res = []

        for word in words:
            res.append(trie.search(word))

        return res