class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        arr = [str(x) for x in range(1,n+1)]
        arr = sorted(arr)

        for i in range(0, n):
            arr[i] = int(arr[i])
        return arr