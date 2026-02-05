class LUPrefix:

    def __init__(self, n: int):
        self.videos = set()
        self.result = 0

    def upload(self, video: int) -> None:
        if video == self.result + 1:
            self.result += 1
        self.videos.add(video)
        
    def longest(self) -> int:
        while self.result + 1 in self.videos:
            self.result += 1
        return self.result
        
# n is the number of videos so 1 2 n
# and the longest rpefix is th eprefix from 1 and counting till itsn o longer incrementing by 1
# we could have an index?
# so we realised 1 is there then we see there's 2 and so forth until we stop or get to end
# and once we stop its like ok cool we store index
# so when we try againwe go back from where we were
# so its just lienar
# oh instead of lienar
# wehave variables
# so want to check if 1 has been added, then move that to 2, etc etc and if so we increment our pointer
# 

# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()