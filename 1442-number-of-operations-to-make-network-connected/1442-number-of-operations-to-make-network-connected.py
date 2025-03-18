class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # find cycles and keep count of avaialble extra wires
        # find amount of wires being used
        # have number of n nodes, need n-1 wires
        # so if number of wires + extra wires meet criteria
        # able achieve
        # itll be n-1 wires - wires used, and if extra wires meet it
        wiresUsed = 0
        wiresExtra = 0
        
        # crucial to create that tree to find cycle
        numberOfEdges = len(connections)
        parents = [i for i in range(numberOfEdges+1)]
        rank = [1] * (numberOfEdges + 1)

        def find(node):
            # traverse and find root if not update it
            if node != parents[node]:
                parents[node] = find(parents[node])
            return parents[node]

        def union(node1, node2):
            # parent of node
            node1, node2 = find(node1), find(node2)

            # edge alreay added, mean extra wire
            if node1 == node2:
                return False
            
            # join by rank aka keeping root consistent
            if rank[node1] > rank[node2]:
                parents[node2] = node1
                rank[node1] += rank[node2]
            else:
                parents[node1] = node2
                rank[node2] += rank[node1]

            # edge not added, means new wire
            return True

        for node1, node2 in connections:
            if not union(node1, node2):
                wiresExtra += 1
            else:
                wiresUsed += 1

        if wiresUsed + wiresExtra >= n-1:
            return (n-1-wiresUsed)
        return -1

        #print(wiresExtra)
       # print(wiresUsed)

            