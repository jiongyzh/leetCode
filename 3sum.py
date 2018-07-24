class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        previous_i = None
        nums.sort()
        for i in range(0, len(nums)-2):
            j = i + 1
            k = len(nums)-1
            if nums[i] == previous_i:
                continue
            else:
                previous_i = nums[i]
            while k > j:
                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j-1] and k > j:
                        j += 1
                    while nums[k] == nums[k+1] and k > j:
                        k -= 1
        return res


if __name__ == '__main__':
    print Solution().threeSum([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0])