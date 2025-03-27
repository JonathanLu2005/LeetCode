class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        # all student has 0
        # positive + 3, negative - 1
        # student id i = report i
        # return top k student after ranking decreasing
        # if multiple student has same point, one with lower id ranks higher
        hashmap = {}

        negative_feedback = set(negative_feedback)
        positive_feedback = set(positive_feedback)

        for i in range(0, len(student_id)):
            id = student_id[i]
            text = report[i]
            text = text.split(" ")
            neg = False
            
            for x in text:
                if x in negative_feedback:
                    hashmap[id] = hashmap.get(id,0) - 1
                elif x in positive_feedback:
                    hashmap[id] = hashmap.get(id,0) + 3

        newHashmap = {}

        values = []

        students = set()
   
        for key, value in hashmap.items():
            if value in newHashmap:
                newHashmap[value].append(key)
            else:
                newHashmap[value] = [key]
                values.append(value)
            students.add(key)

        # rank in decreasing order marks
        if k > len(students):
            remaining = sorted(list(set(student_id) - students))
            newHashmap[0] = remaining
            values.append(0)
        values = sorted(values)[::-1]

        best = []
        i = 0
        if len(values) == 0:
            return sorted(student_id)[:k]
        while k > 0 and i < len(values):    
            value = values[i]

            students = sorted(newHashmap[value])

            for x in students:
                best.append(x)
                k -= 1

                if k == 0:
                    break
            i += 1

        return best

        
            