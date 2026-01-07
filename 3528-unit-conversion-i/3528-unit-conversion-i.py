class Solution:
    def baseUnitConversions(self, conversions: List[List[int]]) -> List[int]:
        # convert this into a tree using hashmap
        # so 0 goes to this and that
        # and can store the rates in (x,y) format
        # then with the first value, we getthe first node all children,and multiply
        # then move to next child or smth
        tree = {}
        rates = {}

        for [src,dst,rate] in conversions:
            if src not in tree:
                tree[src] = []
            tree[src].append(dst)
            rates[(src,dst)] = rate

        n = len(conversions) + 1
        result = [0] * n
        result[0] = 1

        queue = [0]
        while queue:

            for i in range(len(queue)):
                node = queue.pop(0)
                value = result[node]

                for dst in tree[node]:
                    if dst in tree:
                        queue.append(dst)
                    result[dst] = (value * rates[(node,dst)]) % ((10**9)+7)
        #for i in range(0,n):
        #    result[i] = result[i] % ((10**9)+7)
        return result
