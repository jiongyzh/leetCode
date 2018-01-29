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

        return result if result <= 0x7fffffff else 0

