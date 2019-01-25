class Solution(object):
    def nextPermutation0(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return []
        i = j = len(nums) - 1
        while i > 0:
            if nums[i] > nums[i - 1]:
                break
            i -= 1
        if i == 0:
            return nums.sort()
        else:
            while i-1 < j:
                if nums[j] > nums[i-1]:
                    nums[i-1], nums[j] = nums[j], nums[i-1]
                    break
                j -= 1
            nums[i:] = sorted(nums[i:])
        return nums

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-2, -1, -1):
            for j in range(len(nums)-1, i, -1):
                if nums[i] < nums[j]:
                    break
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                nums[i+1:] = sorted(nums[i+1:])
                return
        nums.sort()
        return

if __name__ == '__main__':
    print Solution().nextPermutation([1,3,2])
