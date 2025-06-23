class TrieNode():
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word:str) -> None:
        cur = self.root

        for x in word:
            if x not in cur.children:
                cur.children[x] = TrieNode()
            cur = cur.children[x]
        cur.endOfWord = True

    def search(self, query:str) -> bool:
        cur = self.root

        for x in query:
            if cur.endOfWord:
                return True

            if x not in cur.children:
                return False

            cur = cur.children[x]
        return cur.endOfWord

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.string = ""

        for word in words:
            self.trie.insert(word[::-1])

    def query(self, letter: str) -> bool:
        self.string = letter + self.string
        return self.trie.search(self.string)

# store it backwards, and for each stream create a string and search it backwards to see if exst


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)