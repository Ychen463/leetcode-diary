# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow , fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr= prev, curr,curr.next
        maxSum = 0
        start = head
        while prev:
            maxSum = max(maxSum, start.val+prev.val)
            start = start.next
            prev = prev.next
        return maxSum