class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        # match player to trainer iff player <= trainer abilities
        # return max matchings
        # just be greedy af
        players = sorted(players)
        trainers = sorted(trainers)
        pi = 0
        ti = 0
        res = 0
        pn = len(players)
        tn = len(trainers)

        while pi < pn and ti < tn:
            if players[pi] <= trainers[ti]:
                pi += 1
                ti += 1
                res += 1
            else:
                ti += 1

        return res