class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for key, item in enumerate(nums):
            if item < target:
                continue
            else:
                return key
        return len(nums)

class Solution2(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums)

        if high == 0 or target < nums[0]:
            return 0
        if target > nums[-1]:
            return high

        while low < high:
            mid = (low + high) / 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        if target <= nums[low]:
            return low
        else:
            return low + 1


if __name__ == '__main__':
    print Solution().searchInsert([1, 3, 5, 6], 4)