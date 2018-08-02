class Solution2(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        dp = [[] for _ in xrange(target + 1)]
        dp[0].append([])

        for num in candidates:
            for j in xrange(num, target + 1):
                print 'aa'
                for prev in dp[j - num]:
                    print 'bb'
                    dp[j].append(prev + [num])
                    print num, j, prev
                    print dp[j]
        return dp[-1]


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def get_combination(candidates, target, prefix, res):
            if target == 0:
                res.append(prefix)
                return

            for i in xrange(len(candidates)):
                c = candidates[i]
                if target < c:
                    break
                get_combination(candidates[i:], target-c, prefix + [c], res)

        if not candidates:
            return []
        res = []
        candidates.sort()
        get_combination(candidates, target, [], res)
        return res


if __name__ == '__main__':
    print Solution().combinationSum([2,3,5], 8)
