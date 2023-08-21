class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        merged[]
        i = 0
        j = 0
        while (i< len(nums1) || j < len(nums2)):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                if (i + 1 < len(nums1)):


                    i = i + 1 
            elif nums1[i] > nums2[j]):
                merged.append(nums2[j])
                if (j + 1 < len(nums2)):
                    j = j + 1
            else:
                if (i + 1 < len(nums1)):

                    i = i + 1 
                if (j + 1 < len(nums2)):
                    j = j + 1
        return merged[(len(merged)-1)//2]
