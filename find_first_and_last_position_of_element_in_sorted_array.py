class Solution2(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        first = last = 0

        # get the end place
        low = 0
        high = len(nums)
        while low < high:
            mid = (low + high) / 2
            if target < nums[mid]:
                high = mid
            else:
                low = mid + 1
        last = low - 1

        # get the start place
        low = 0
        high = len(nums)
        while low < high:
            mid = (low + high) / 2
            if target > nums[mid]:
                low = mid + 1
            else:
                high = mid
        first = low

        if first == last + 1 :
            return [-1, -1]

        return [first, last]


class Solution3(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        first = last = low = 0
        high = len(nums)
        while low < high:
            mid = (low + high) / 2
            if target > nums[mid]:
                low = mid + 1
            else:
                high = mid
        first = low

        if first >= len(nums) or nums[first] != target:
            return [-1, -1]
        else:
            while low < len(nums):
                low += 1
                if low >= len(nums) or nums[first] != nums[low]:
                    low -= 1
                    break
            last = low

        return [first, last]


class Solution1(object):
    def searchRange(self, nums, target):
        import bisect
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        upper = bisect.bisect_right(nums, target)
        lower = bisect.bisect_left(nums, target)
        if upper == lower:
            return (-1,-1)
        return (lower,upper-1)


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) / 2
            if nums[mid] == target:
                sta = end = mid
                while sta > 0 and nums[sta] == target:
                    sta -= 1
                while end < len(nums) and nums[end] == target:
                    end += 1
                if nums[sta] != target:
                    sta += 1
                if end == len(nums) or nums[end] != target:
                    end -= 1
                return [sta, end]
            else:
                if nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid -1
        return [-1, -1]


if __name__ == '__main__':
    print Solution2().searchRange([1,2,3,3,3,4,5,6], 3)