# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = ""
        s2 = ""

        while l1 is not None:
            s1 += str(l1.val)
            l1 = l1.next 
        while l2 is not None: 
            s2 += str(l2.val)
            l2 = l2.next

        add = (str(int(s1[::-1]) + int(s2[::-1])))[::-1]

        newNode = ListNode()
        dummy = newNode

        for c in add:
            c = int(c)
            newNode.next = ListNode(c, None)
            newNode = newNode.next

        return dummy.next

        """
        go through both and keep adding

        dummy = ListNode() 
        cur = dummy
        
        carry = 0
        while l1 or l2 or carry:
            # so even if we lose 1, can keep going
            v1 = l1.val if l1 else 0 
            v2 = l2.val if l2 else 0
            
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10

            cur.next = ListNode(val)

            cur = cur.next
            l1 = l1.next if l1 else None 
            l2 = l2.next if l2 else None

        # look out for carry 
        return dummy.next
        """