class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # identifyy cycle and edges, then able find which one is last one
        # have N nodes, need N - 1 edges
        # union find - add edges and nodes, will tell us when we add an edge to a component that exists
        # aka introduce cycle
        # connect edges to "root"
        # mean once we add an edge that exists, itll detect its there 
        # path compression + union by rank O(V+E
        
        # hold parent of every node
        n = len(edges)

        # parent is itself
        parents = [i for i in range(n+1)]

        # ranks
        rank = [1] * (n+1)

        def find(n):
            # parent of itself
            if n != parents[n]:
                parents[n] = find(parents[n])

            # go up the chain until we get to the root
            return parents[n]
        
        def union(n1, n2):
            # find parent of node
            p1, p2 = find(n1), find(n2)

            # connected already, detected cycl
            if p1 == p2:
                return False

            # union by rank
            if rank[p1] > rank[p2]:
                parents[p2] = p1
                rank[p1] += rank[p2]
            else:
                parents[p1] = p2
                rank[p2] += rank[p1]
            # if not c onnected already
            return True

        for n1, n2 in edges:
            # redundant edge
            if not union(n1, n2):
                return [n1, n2]

        """
        hashmap = {}


        for [src, dst] in edges:
            if src not in hashmap:
                hashmap[src] = [dst]
            else:
                hashmap[src].append(dst)

            if dst not in hashmap:
                hashmap[dst] = [src]
            else:
                hashmap[dst].append(src)

        print(hashmap)

        # go backweards through edges
        # and if both lists are > 1 its that one!
        for [src, dst] in edges[::-1]:
            if len(hashmap[src]) > 1 and len(hashmap[dst]) > 1:
                return [src, dst]
        """