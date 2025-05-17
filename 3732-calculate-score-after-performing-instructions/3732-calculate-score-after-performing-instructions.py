class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        # if i instruction add, add to value, move to instruction i + 1
        # if instruction jump move to i + values[i] instruction
        # if out of bounds we end
        # if we revisit executed instruction (use set to store) not executed
        score = 0
        i = 0
        visited = set()
        n = len(values) 

        while True:
            # stop
            if i in visited or i < 0 or i >= n:
                break

            # else add instruction we'll execute
            visited.add(i)
            instruction = instructions[i]

            # if add move by 1 and add value
            if instruction == "add":
                score += values[i]
                i += 1
            # else jump
            else:
                i += values[i]

        return score

        # i=0, jump 3, i=3, jump -1, i=2, add 12