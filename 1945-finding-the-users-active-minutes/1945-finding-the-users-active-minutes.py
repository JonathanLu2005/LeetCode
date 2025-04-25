class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        # log is ID and time, perofrmed at time
        # users can perofrm at same time, user can do multiple actions at same time
        # UAM = num of unique min, where user perform action on LC
        # only counted once
        # so for each ID, get their UAM, and in array from 0 to k, index is UAM and how many are in there
        answers = [0] * k
        hashmap = {}

        for [ID, minute] in logs:
            if ID not in hashmap:
                hashmap[ID] = set()
            hashmap[ID].add(minute)

        for ID, UAM in hashmap.items():
            answers[len(UAM) - 1] += 1
        return answers