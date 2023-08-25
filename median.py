from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        merged = []
        i = 0
        j = 0
        while ( i < len(nums1) and j < len(nums2) ):
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i = i + 1
            if nums1[i] >= nums2[j]:
                merged.append(nums2[j])
                j = j + 1
        merged.extend(nums1[i:])
        merged.extend(nums2[j:])
        if (len(merged) & 1) and len(merged) >= 1:
            return (merged[len(merged)//2]+merged[len(merged)//2-1])/2
        elif len(merged) > 2:
            return (merged[len(merged)//2]+merged[len(merged)//2-1])/2
if __name__ == "__main__":

    a = Solution()
    print( a.findMedianSortedArrays([1,8,23,24], [9,10,11]))
    print( a.findMedianSortedArrays([1,2,3,4], [5,6,7]))
    print( a.findMedianSortedArrays([1,2,3,8], [5,6,7]))
    print( a.findMedianSortedArrays([1,2,3,4], [1,2,3]))

