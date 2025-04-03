class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        """
        find the biggest number and let them spread with k amount, and take over the smallest number, and keep going
        and we'll have to store this somewhere, altho this might be a bit complicated
        alternatively, i could go through each number in array
        do the same tactic where it spreads about for k amount
        and the one thats bigger takes the place but idk
        """

        """
        n = len(arr)
        dp = [0] * (n)
        
        for i in range(0, n):
            # val we're on
            current = arr[i]

            for j in range(i - k - 1, i + k - 1):
                if j >= 0 and j < n:
                    change = arr[j]

                    dp[j] = max(dp[j], arr[i], arr[j])
        
        print(dp)
        return sum(dp)
        """
        
        # create dp array
        n = len(arr)
        dp = [0] * (n+1)

        # go through each part of dp
        for i in range(1, n+1):
            maxValue = 0

            # find max value in partition
            # check different partitions
            # get max value and add it to the sum
            for j in range(1, min(k,i) + 1):
                maxValue = max(maxValue, arr[i-j])
                dp[i] = max(dp[i], dp[i-j] + maxValue * j)
        return dp[n]