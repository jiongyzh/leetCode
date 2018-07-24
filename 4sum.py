class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        if nums:
            nums.sort()
            self.get_n_sum(nums, target, [], res, 4)
        return res

    def get_n_sum(self, nums, target, pre_res, res, n_sum):
        if target < nums[0] * n_sum or target > nums[-1] * n_sum or len(nums) < n_sum:
            return
        if n_sum == 2:
            i, j = 0, len(nums) - 1
            while i < j:
                s = nums[i] + nums[j]
                if s == target:
                    res.append(pre_res + [nums[i], nums[j]])
                    i += 1
                    while nums[i] == nums[i - 1] and i < j:
                        i += 1
                elif s < target:
                    i += 1
                else:
                    j -= 1
        else:
            for i in range(0, len(nums)-n_sum+1):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                self.get_n_sum(nums[i+1:], target-nums[i], pre_res+[nums[i]], res, n_sum-1)
        return


if __name__ == '__main__':
    print Solution().fourSum([1, 0, -1, 0, -2, 2], 0)