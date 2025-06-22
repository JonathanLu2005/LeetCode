# node for trie
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:

    def __init__(self):
        # create root
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        # create new word
        cur = self.root

        for c in word:
            # check if eixst in trie

            # c not in node children
            if c not in cur.children:
                # crete trie node
                cur.children[c] = TrieNode()
            # else continue, access node 
            cur = cur.children[c]
        # signal this for search
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        # start at root
        cur = self.root

        for c in word:
            # stop existing
            if c not in cur.children:
                return False
            cur = cur.children[c]

        # once stop need check if is end of word
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        #start at root
        cur = self.root

        for c in prefix:
            # stop exist
            if c not in cur.children:
                return False
            cur = cur.children[c]

        # else all good
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)