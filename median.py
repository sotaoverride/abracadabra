class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        merged[]
        i = 0
        j = 0
        while (i< len(nums1) || j < len(nums2)):
            #here
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i++
            elif nums1[i] > nums2[j]):
                merged.append(nums2[j])
                j++
            else:
                merged.append(nums2[j])
                merged.append(nums2[j])
                i++
                j++
        return merged[(len(merged)-1)//2]
