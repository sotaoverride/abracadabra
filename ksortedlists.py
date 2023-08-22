# Definition for a singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) - > Optional[ListNode]):
        ListNode merged
        merged.val = 0
        merged.next = None
        for i in lists:
            #
            current_new = i
            tmp_new = current
            while current_new.next is not None:
                #
                while current_new.val < merged.val:
                    tmp = current_new
                    current_new = current_new.next
                tmp.next = merged
                current_new = tmp
                


