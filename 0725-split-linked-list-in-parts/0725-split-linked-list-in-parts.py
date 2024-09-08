# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        if k == 1:
            return [head]
        
        # Count the total number of nodes
        count = 0
        current = head
        while current:
            count += 1
            current = current.next
        
        arr = [None] * k

        if count <= k:
            for i in range(count):
                arr[i] = head
                tail = head
                head = head.next
                tail.next = None
            return arr
        
        extraCount = count % k
        elementsCount = count // k

        for i in range(k):
            arr[i] = head
            currentPartSize = elementsCount + (1 if extraCount > 0 else 0)
            extraCount -= 1

            for j in range(currentPartSize - 1):
                head = head.next

            if head:
                tail = head
                head = head.next
                tail.next = None

        return arr