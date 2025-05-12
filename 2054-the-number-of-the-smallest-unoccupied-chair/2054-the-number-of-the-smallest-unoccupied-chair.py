class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        # n friends 0 to n-1 attend
        # chair are 0 to inf
        # frined sit on smallest unoccupied chair
        # when leave, chair is free
        # time are arrival and leaving for ith friend
        # n friends, chairs are just n chairs tbf
        # and given a speciifc friend see what chair
        # store each time = ith friend, then sort it so we can see whats going on
        # for each chair taken put in time itll be free, and if arrival time >= leave time then can take it!
        n = len(times)
        chairs = [0] * n
        hashmap = {}

        for i in range(0, n):
            time = times[i]
            x, y = time[0], time[1]

            hashmap[(x,y)] = i

        res = 0

        times = sorted(times)

        for [arr, lev] in times:
            for i in range(0, n):
                chair = chairs[i]

                if arr >= chair:
                    chairs[i] = lev
                    if hashmap[(arr,lev)] == targetFriend:
                        return i
                    break
        

        
        

