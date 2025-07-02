class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        # edge case is if same
        if sx == fx and sy == fy:
            if t != 1:
                return True
            return False
        
        
        # either take horizontal or vertical steps to get there
        difference = max(abs(fx-sx), abs(sy-fy))
        

        if difference <= t:
            return True
        return False
