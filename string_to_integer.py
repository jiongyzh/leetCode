class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        s_clean = ''
        sign = 1
        s = str.strip()
        if s == '':
            return 0
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        for x in s:

            if '0' <= x <= '9':
                s_clean += x
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

