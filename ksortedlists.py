from typing import List, Optional
# Definition for a singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        merged = []
        unsorted = []
        total_nodes = 0
        #convert array of linked lists to array of simple arrays.
        for l in lists:
            arr = []
            while l.next is not None:
                arr.append(l.val)
                total_nodes = total_nodes + 1
                l = l.next
            arr.append(l.val)
            total_nodes = total_nodes + 1
            unsorted.append(arr)
        print(unsorted)
        # set up arrays to keep track of sizes and indexes of each array
        total_lists = len(unsorted)
        lists_index=[None]*(total_lists)
        lists_size=[None]*(total_lists)
        # init sizes and indexes to zero
        for i in range(len(lists_index)):
            lists_size[i] = len(unsorted[i])
            lists_index[i] = 0
        # now do an insertion sort style thing on all arrays
        tmp = 0
        min = 500
        index = None
        while tmp < total_nodes:
            for i in range(len(lists_index)):
                if lists_index[i] < len(unsorted[i]):
                    if i == 0:
                        min = unsorted[i][lists_index[i]]
                        index = i
                    if unsorted[i][lists_index[i]] <= min:
                        min = unsorted[i][lists_index[i]]
                        index = i
            merged.append(min)
            lists_index[index] = lists_index[index] + 1
            tmp = tmp + 1
        tmp_n = ListNode()
        head = ListNode()
        head = tmp_n
        print(merged)
        #convert sorted array to a linked list
        for n in merged:
            tt = ListNode()
            tt.val = n
            while tmp_n.next != None:
                tmp_n=tmp_n.next
            tmp_n.next = tt

 

        return head

if __name__ == "__main__":
    a = Solution()
    tmp = ListNode()
    tmpa = ListNode()
    tmpc = ListNode()
    tmpd = ListNode()
    tmp.val = 1
    tmp.next = tmpa
    tmpa.val = 2
    tmpa.next = tmpc
    tmpc.val = 3
    tmpc.next = tmpd
    tmpd.val = 4
    tmpd.next = None
    tmpMerged = ListNode()
    tmpMerged=a.mergeKLists([tmp, tmp, tmp])
    while tmpMerged is not None:

        print(tmpMerged.val)
        tmpMerged = tmpMerged.next

