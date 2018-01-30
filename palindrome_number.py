class Solution(object):
    def isPalindrome1(self, x):
        """
        :type x: int
        :rtype: bool
        """

        len_x = len(str(x))
        while len_x > 1:
            len_x = len(str(x))
            x_head = x / 10 ** (len_x - 1)
            x_tail = x % 10
            if x_head == x_tail:
                x = x - x_head * 10 ** (len_x - 1)
                x = (x - x % 10) / 10
            else:
                return False

            i = len_x - len(str(x)) - 2
            if i > 0:
                if x % 10 ** i != 0:
                    return False
                else:
                    x = x / 10 ** i

        return True

    # Reverse
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x % 10 == 0 and x != 0:
            return False

        i = 0
        while i < x:
            i = i * 10 + x % 10
            x = x / 10

        return True if i == x or i / 10 == x else False




if __name__ == '__main__':
    print Solution().isPalindrome(10021)