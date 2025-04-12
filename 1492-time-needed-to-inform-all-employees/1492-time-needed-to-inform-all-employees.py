class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # n employees with id 0 to n-1
        # head has head id
        # employee has manager where amnager i is manager of employee
        # tree structure
        # i-th employee need inform time minute to inform suborindates
        # return num minutes to inform employee
        # hashmap, manager = subordinates
        # then bfs and apply inform time 
        # only if they've subordinates

        if n <= 1:
            return 0

        hashmap = {}

        for emp in range(0, n):
            if emp != headID:
                m = manager[emp]
                if m not in hashmap:
                    hashmap[m] = []
                hashmap[m].append(emp)

        queue = deque([(headID, 0)])
        res = 0
        # bfs want longest branch
        while queue:
            curNode, curTime = queue.popleft()
            res = max(res, curTime)

            if curNode in hashmap:
                for sub in hashmap[curNode]:
                    queue.append((sub, curTime + informTime[curNode]))

        return res