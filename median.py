from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []
        i = 0
        j = 0
        while ( i < len(nums1) and j < len(nums2) ):
            x = nums1[i]
            y = nums2[j]
            if x <= y:
                merged.append(x)
                i = i + 1
            if y <= x:
                merged.append(y)
                j = j + 1
        merged.extend(nums1[i:])
        merged.extend(nums2[j:])
        if (len(merged) & 1) and len(merged) >= 1:
            if(len(merged) is (len(nums1) + len(nums2))):
                #
                return merged[(len(merged)-1)//2]
        elif len(merged) > 2:
            if(len(merged) is (len(nums1) + len(nums2))):
                return (merged[len(merged)//2]+merged[len(merged)//2-1])/2

if __name__ == "__main__":
    a = Solution()
    print( a.findMedianSortedArrays([1,8,23,24], [9,10,11]))
    print( a.findMedianSortedArrays([1,2,3,4], [5,6,7]))
    print( a.findMedianSortedArrays([1,2,3,8], [5,6,7]))
    print( a.findMedianSortedArrays([1,2,3,4], [1,2,3]))
    print( a.findMedianSortedArrays([1,5,6,9], [1,2,7,10,20]))
    print( a.findMedianSortedArrays([1,5,6,9], [1,2,3,7,10,20]))

