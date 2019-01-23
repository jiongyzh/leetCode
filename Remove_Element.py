class Solution(object):
    def removeElement0(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        interval = 0
        for i in range(len(nums)):
            if nums[i] == val:
                interval += 1
            else:
                nums[i-interval] = nums[i]
        return len(nums) - interval

    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        i = j = 0
        # while is faster than in range
        while i < len(nums):
            if nums[i] != val:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
            i += 1
        return j
