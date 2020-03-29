# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        front = head
        i=0
        while front != None and i < n:
            front = front.next
            i=i+1

        behind = ListNode()
        newhead = behind
        behind.next = head
        while front != None:
            front = front.next
            behind = behind.next
        behind.next = behind.next.next
        return newhead.next
