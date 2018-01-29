class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total_length =  len(nums1) + len(nums2)

        # there are two median numbers
        if total_length % 2 == 0:
            return (self.get_Kth(nums1, 0, nums2, 0, total_length/2) +
                    self.get_Kth(nums1, 0, nums2, 0, total_length/2 + 1)) / 2.0

        # only one median number
        return Solution.get_Kth(nums1, 0, nums2, 0, total_length/2 +1)

    @staticmethod
    # return Kth number
    def get_Kth(l1, start1, l2, start2, k):
        if start1 >= len(l1):
            return l2[start2 + k - 1]

        if start2 >= len(l2):
            return l1[start1 + k - 1]

        if k == 1:
            return min(l1[start1], l2[start2])

        key1 = (l1[start1 + k/2 - 1] if start1 + k/2 - 1 < len(l1) else float('inf'))
        key2 = (l2[start2 + k/2 - 1] if start2 + k/2 - 1 < len(l2) else float('inf'))

        if key1 < key2:
            return Solution.get_Kth(l1, start1 + k/2, l2, start2, k - k/2)
        else:
            return Solution.get_Kth(l1, start1, l2, start2 + k/2, k - k/2)


if __name__ == '__main__':
    print Solution().findMedianSortedArrays([1,2,3,4,5,6,7], [1,2])