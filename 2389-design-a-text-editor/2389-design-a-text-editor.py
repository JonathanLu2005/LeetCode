class TextEditor:

    def __init__(self):
        self.left = []
        self.right = []

    def addText(self, text: str) -> None:
        self.left.extend(text)

    def deleteText(self, k: int) -> int:
        result = min(k, len(self.left))

        for x in range(result):
            self.left.pop()
        return result

    def cursorLeft(self, k: int) -> str:
        # if we move left k times, that means k on elft move to start of right
        result = min(k,len(self.left))

        for x in range(result):
            self.right.append(self.left.pop())
        return "".join(self.left[-10:])

    def cursorRight(self, k: int) -> str:
        # if we move right, that means whatever on left of right, move to left
        result = min(k,len(self.right))
        
        for x in range(result):
            self.left.append(self.right.pop())
        return "".join(self.left[-10:])
        
# have array no? so we can use indices to easily insert or pop wherever
# alongside able insert where cursor will be
# then everytime we move it, show left of it min(10 or howmuch there is)

# have 2 stacks, when inserting its actually O(n) because of shifting the elements

# again still inserting, its not good as will need arrange elements
# have the right array be other way round, s.t. index 0 is very end 
# and index -1 is very start, hence only need to append
# also dont need cursor integer avriable, can just make sure that k or length is within capacity
# to make the moves


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)