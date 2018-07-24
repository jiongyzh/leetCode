class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(0, len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i + 1, len(nums) - 1
            while k > j:
                s = nums[i] + nums[j] + nums[k]
                if s > 0:
                    k -= 1
                elif s < 0:
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

    # better performance
    def threeSum2(self, nums):
        if len(nums) < 3:
            return []

        res = []
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        if 0 in dic and dic[0] > 2:
            res.append([0, 0, 0])

        pos = []
        neg = []
        for k in dic:
            if k > 0:
                pos.append(k)
            elif k < 0:
                neg.append(k)
        pos.sort()
        neg.sort()

        for i in pos:
            for j in neg:
                if -(i + j) in dic:
                    if (-(i + j) == i) and dic[i] > 1:
                        res.append([j, -(i + j), i])
                    elif (-(i + j) == j) and dic[j] > 1:
                        res.append([j, -(i + j), i])
                    elif j < -(i + j) < i:  # insure no duplicates
                        res.append([j, -(i + j), i])
        return res


if __name__ == '__main__':
    print Solution().threeSum2([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0])