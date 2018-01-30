class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        s_clean = ''
        sign = 1
        s = str.strip()

        for i in range(len(s)):
            if '0' <= s[i] <= '9':
                s_clean += s[i]
            elif i == 0:
                if s[i] == '-':
                    sign = -1
                elif s[i] == '+':
                    pass
                else:
                    return 0
            else:
                break

        if s_clean:
            result = sign * int(s_clean)
        else:
            return 0

        if result > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if result < -2 ** 31:
            return -2 ** 31

        return result

