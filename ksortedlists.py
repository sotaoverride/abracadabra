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
        current = None
        for i in range(len(lists)):
            #here
            current = lists[i]
            flag = False
            while current.next is not None:
                while merged is not None:
                    if current.val > merged.val:
                        if merged.next is not None:
                            if merged.next.val < current.val:
                                tmp = merged.next
                                merged.next = current
                                current.next = tmp
                                flag = True
                if not flag:
                    merged.next = current
                current = current.next
                flag = False
                


