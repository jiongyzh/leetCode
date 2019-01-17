class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        prefix = strs[0]
        for i in range(1, len(strs)):
            while len(prefix) > 0:
                if strs[i].startswith(prefix):
                    break
                else:
                    prefix = prefix[:-1]
        return prefix

    def longestCommonPrefix2(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        prefix = strs[0]
        for i in range(0, len(prefix)):
            for j in range(1, len(strs)):
                try:
                    if prefix[i] == strs[j][i]:
                        continue
                    else:
                        return prefix[:i]
                except IndexError:
                    return prefix[:i]
        return prefix

    @staticmethod
    def longest_common_prefix(strs, l, r):
        if l == r:
            return strs[l]
        else:
            m = (l + r) / 2
            llc = Solution.longest_common_prefix(strs, l, m)
            rlc = Solution.longest_common_prefix(strs, m + 1, r)
            if not llc or not rlc:
                return ''
            for i in range(len(llc)):
                try:
                    if llc[i] == rlc[i]:
                        continue
                    else:
                        return llc[:i]
                except IndexError:
                    return rlc
            return llc

    def longestCommonPrefix3(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        return Solution.longest_common_prefix(strs, 0, len(strs) - 1)

    # def longestCommonPrefix4(self, strs):
    #     """
    #     :type strs: List[str]
    #     :rtype: str
    #     """
    #     if not strs:
    #         return ''
    #     print 'ccc'
    #     if len(strs) == 1:
    #         return strs[0]
    #     prefix = strs[0]
    #     low = mid = 0
    #     high = len(prefix)
    #     print low, high
    #     while low < high:
    #         print 'bbbb'
    #         mid = (low + high) / 2
    #         for i in range(1, len(strs)):
    #             print 'aaaa:', i
    #             if strs[i].startswith(prefix[:mid]):
    #                 continue
    #             else:
    #                 if mid == 0:
    #                     return ''
    #                 high = mid - 1
    #                 break
    #         if mid == 0:
    #             return prefix[mid]
    #         if high > mid:
    #             low = mid + 1
    #     return prefix[:mid]

    def longestCommonPrefix4(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        def is_common_prefix(strs, l):
            for i in range(1, len(strs)):
                if not strs[i].startswith(strs[0][:l]):
                    return False
            return True

        if not strs:
            return ''
        low = 0
        high = len(strs[0])
        while low <= high:
            mid = (low + high) / 2
            print strs[0][:mid]
            if is_common_prefix(strs, mid):
                low = mid + 1
            else:
                high = mid - 1
        print (low + high) / 2

        return strs[0][:(low + high) / 2]

    def longestCommonPrefix5(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Exception if strs empty
        if not strs:
            return ''

        # Getting smallest string length
        min_size = float('inf')
        for string in strs:
            min_size = min(min_size, len(string))

        # Iterating till the smallest string length
        for index in range(min_size):
            # Assigning character of first string
            char = strs[0][index]

            # Checking if it is the same for all strings
            for string in strs:
                if string[index] != char:
                    # returning trimmed string till the current index
                    return string[:index]

        # Returning smallest string
        return strs[0][:min_size]


if __name__ == '__main__':
    print Solution().longestCommonPrefix4(["flowe","flow","flight"])
    print Solution().longestCommonPrefix4(["aa", "aa"])
    print Solution().longestCommonPrefix4(["a", "ab"])