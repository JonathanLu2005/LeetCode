class Solution:
    def maxBalancedShipments(self, weight: List[int]) -> int:
        # balance if in a shipment, the last parcel is < biggest
        # well the algorithm can work in linear time
        # first package is our target
        # if next i <, ok thats a shipment yay
        # otherwise that package is the next biggest target
        result = 0
        target = weight[0]
        n = len(weight)
        i = 1

        while i < n:
            current = weight[i]

            if current < target:
                result += 1
                if i + 1 < n:
                    target = weight[i+1]
                i += 1
            else:
                target = current
            i += 1
        return result