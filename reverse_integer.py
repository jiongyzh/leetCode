class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return -self.reverse(-x)
        if x == 0:
            return 0

        result = 0

        while x > 0:
            result = result * 10 + x % 10
            x /= 10

        return result if result < 0x80000000 else 0

    def reverse2(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            x = -int(str(abs(x))[::-1])
        else:
            x = int(str(x)[::-1])

        return x if (x >= -2 ** 31 and x < 2 ** 31) else 0


