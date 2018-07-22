class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]

        i = 0
        res = 0
        while s:
            if s.startswith(syb[i]):
                res += val[i]
                s = s.replace(syb[i], '', 1)
            else:
                i += 1
        return res


if __name__ == '__main__':
    print Solution().romanToInt('LX')
