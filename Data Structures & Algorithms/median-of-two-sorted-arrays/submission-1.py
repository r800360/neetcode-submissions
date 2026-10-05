class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m = len(nums1)
        n = len(nums2)
        
        left = 0
        right = m

        half = (m + n + 1) // 2

        while (left <= right):
            i = (left + right) // 2
            j = half - i

            A_left = nums1[i - 1] if i > 0 else float("-inf")
            A_right = nums1[i] if i < m else float("inf")

            B_left = nums2[j - 1] if j > 0 else float("-inf")
            B_right = nums2[j] if j < n else float("inf")

            if A_left > B_right:
                right = i - 1
                continue
            
            if B_left > A_right:
                left = i + 1
                continue
            
            if (m + n) % 2 == 1:
                return max(A_left, B_left)
            
            return ( max(A_left, B_left) + min(A_right, B_right) ) / 2
            