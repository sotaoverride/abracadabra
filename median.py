class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        merged[]
        j = 0
        for i,element in enumerate(nums1):

            if element < nums2[j]:
                merged.append(element)
            else:
                merged.append(nums2[j])
                j++
        if j < len_nums2-1:
            merged.extend(nums2[j:])
        return merged[(len(merged)-1)//2]
