class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # have n boxes
        # string is length n
        # 0 = empty, 1 = 1 ball
        # may move 1 ball to adjacent box
        # return answer i s.t. is min num operations to move all balls to that box
        
        # i mean we can only move to adjacent
        # so for how many balls we've in the box, to move it to the other box
        # its gonna be number of balls x distance i-j abs

        # brute force is n^2
        result = []
        n = len(boxes)

        for i in range(0,n):
            moves = 0

            for j in range(0,n):
                ball = boxes[j]

                if ball == "1":
                    distance = abs(i-j)
                    moves += (distance)
            result.append(moves)
        return result