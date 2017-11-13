class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = dict()
        i = 0
        while i < len(nums):
            if target-nums[i] in d:
                return [d[target-nums[i]], i]
            d[nums[i]] = i
            i += 1
        return None


if __name__ == '__main__':
    print Solution().twoSum((2, 7, 11, 15), 18)
