class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def gen_valids(n, pre, cnt, ans):
            if len(pre) == 2 * n:
                if cnt == 0:
                    ans.append(pre)
                return

            if cnt < 0 or cnt > n:
                return

            gen_valids(n, pre + '(', cnt + 1, ans)
            gen_valids(n, pre + ')', cnt - 1, ans)

        res = []
        gen_valids(n, '', 0, res)
        return res

class Solution1(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def backtrack(total_left, total_right, total, curr_str, res):
            if total_left + total_right == total:
                res.append(curr_str)
                return
            if total_left < total / 2:
                curr_str += '('
                backtrack(total_left + 1, total_right, total, curr_str, res)
                curr_str = curr_str[:-1]
            # compare before processing to get better performance
            if total_right < total_left:
                curr_str += ')'
                backtrack(total_left, total_right + 1, total, curr_str, res)

        res = []
        backtrack(0, 0, n * 2, '', res)
        return res

class Solution2(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        if n == 0:
            return ['']

        li = [('(', 1)]
        for i in range(1, 2 * n):
            s = []
            for p, c in li:
                if 2 * n - i > c:
                    s.append((p + '(', c + 1))

                if c > 0:
                    s.append((p + ')', c - 1))
            li = s

        res = []
        for p, c in li:
            res.append(p)
        return res


if __name__ == '__main__':
    print Solution().generateParenthesis(4)

