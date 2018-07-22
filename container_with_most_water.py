class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        idx_head = 0
        idx_tail = len(height) - 1
        max_volume = 0

        while idx_head != idx_tail:
            max_volume = max(max_volume, min(height[idx_head], height[idx_tail]) * (idx_tail - idx_head))
            if height[idx_head] >= height[idx_tail]:
                idx_tail -= 1
            else:
                idx_head += 1
        return max_volume


if __name__ == '__main__':
    print Solution().maxArea([3,2,4,8,5,6])