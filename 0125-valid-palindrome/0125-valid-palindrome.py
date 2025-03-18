class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = []

        for c in s:
            if c.isalnum():
                arr.append(c.lower())

        p1 = 0
        p2 = len(arr) - 1

        while p1 <= p2:
            if arr[p1] == arr[p2]:
                p1 += 1
                p2 -= 1
            else:
                return False 

        return True