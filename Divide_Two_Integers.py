class Solution(object):
    def divide0(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        def divide(n_divid):
            tmp = 0
            while n_divid >= divis:
                tmp += 1
                n_divid -= divis
            print tmp, n_divid
            return tmp, n_divid

        divid = abs(dividend)
        divis = abs(divisor)
        if divis > divid:
            return 0
        sign = 1
        if (divisor < 0 < dividend) or (dividend < 0 < divisor):
            sign = -1

        s_divid = str(divid)
        s_divis = str(divis)

        pre = s_divid[:len(s_divis)-1]
        res = []

        for i in range(len(s_divis)-1, len(s_divid)):
            q, r = divide(int(pre + s_divid[i]))
            pre = str(r)
            res.append(str(q))

        res = int(''.join(res)) * sign
        if res > 2**31 - 1 or res < -2**31:
            return 2**31 - 1
        return res


    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        divid = abs(dividend)
        divis = abs(divisor)
        if divis > divid:
            return 0

        res = 0
        while divid >= divis:
            tmp, i = divis, 1
            while divid >= tmp:
                divid -= tmp
                res += i
                tmp += tmp
                i += i

        if (divisor < 0 < dividend) or (dividend < 0 < divisor):
            res = -res

        if res > 2**31 - 1 or res < -2**31:
            return 2**31 - 1

        return res

if __name__ == '__main__':
    Solution().divide(-2147483648, -1)
