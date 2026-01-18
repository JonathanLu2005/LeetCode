class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # find longest substring without any duplicate characters
        track = set()
        start = 0
        result = 0
        current = 0
        n = len(s)

        for i in range(0,n):
            letter = s[i]

            if letter in track:
                result = max(result,current)

                while letter in track:
                    left = s[start]
                    track.remove(left)
                    current -= 1
                    start += 1
                
            current += 1
            track.add(letter)
        result = max(result,current)
        return result