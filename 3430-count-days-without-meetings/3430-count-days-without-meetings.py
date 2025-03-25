class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings = sorted(meetings)

        # if end of one before overalp with start of another

        i = 0

        while i < len(meetings) - 1:
            current = meetings[i]
            nextmeeting = meetings[i+1]

            if current[1] >= nextmeeting[0]:
                newStart = min(current[1], current[0], nextmeeting[0], nextmeeting[1])
                newEnd = max(current[1], current[0], nextmeeting[0], nextmeeting[1])

                newMeeting = [newStart, newEnd]
                meetings.pop(i)
                meetings.pop(i)
                meetings.insert(i, newMeeting)
            else:
                i += 1

        for start, end in meetings:
            days -= (end - start + 1)
        return days
