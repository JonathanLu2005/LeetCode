class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        # value in array is the node its being pointed to
        # plus valie of i

        hashmap = {}

        for i in range(0,len(edges)):
            node = edges[i]

            hashmap[node] = hashmap.get(node,0) + i

        nodeResult = 0
        valueResult = 0

        for key, value in hashmap.items():
            if value > valueResult:
                valueResult = value

                nodeResult = key
            elif value == valueResult:
                if key < nodeResult:
                    nodeResult = key
        
        return nodeResult