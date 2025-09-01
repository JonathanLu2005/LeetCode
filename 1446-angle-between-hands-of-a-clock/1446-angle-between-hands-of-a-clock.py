class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # 360 degrees
        # 1 minute = 6 degrees
        # so minutes * 6
        # likewise for hours, 12 hours
        # 360 / 12 = 30
        # times by minutes / 60
        # so 15 and 180, so 165
        # calculate difference by time - time
        # or 360 - massive + smallest
        minuteDegree = minutes * 6
        minuteFraction = minutes / 60

        if hour == 12:
            hour = 1
        else:
            hour += 1

        hourDegree = (30 * minuteFraction) + ((hour-1) * 30)

        time = abs(hourDegree - minuteDegree)

        return min(time, 360-time)