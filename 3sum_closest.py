class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = sum(nums[:3])

        for i in range(len(nums)-2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                temp = sum((nums[i], nums[l], nums[r]))
                if abs(temp - target) < abs(res - target):
                    res = temp
                if temp < target:
                    l += 1
                elif temp > target:
                    r -= 1
                else:
                    return res
        return res


if __name__ == '__main__':
    print Solution().threeSumClosest([-1, 2, 1, -4],1)