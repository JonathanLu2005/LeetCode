class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.TTL = timeToLive
        self.hashmap = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.hashmap[tokenId] = currentTime + self.TTL

    def renew(self, tokenId: str, currentTime: int) -> None:
        value = self.hashmap.get(tokenId,-1)

        if currentTime < value:
            self.hashmap[tokenId] = currentTime + self.TTL

    def countUnexpiredTokens(self, currentTime: int) -> int:
        tokens = self.hashmap.values()

        return len([x for x in tokens if x > currentTime])
        
# receive token that'll expire at TTL after CT
# if renewed, TTL will change

# we have the same TTL, then given tokens at CT, have TTL
# if renewed, only renew if unexpired
# then given a CT, return num of unepxired tokens

# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)