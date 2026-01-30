# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # return node where cycle begins
        # else return null
        # return POSITION of the node when cycle begins
        # cycle -> we reach to a node and realise it alrdy been visited
        # when find node, store position in hashmap as we go so we can return that
        # return null if we cant traverse anymore aka node next is none
        if head is None:
            return None
        hashmap = {}
        visited = set()

        node = head
        while node.next:
            if node not in visited:
                visited.add(node)
                hashmap[node] = node
                node = node.next
            else:
                return hashmap[node]
        return None