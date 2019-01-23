class Solution(object):
    def removeElement(self, nums, val):
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
