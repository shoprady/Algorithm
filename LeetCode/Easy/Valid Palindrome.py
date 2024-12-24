import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub('[^a-zA-Z0-9]', '', s)
        s = s.lower()

        length = len(s)

        if length <= 1:
            return True

        for i in range(length / 2):
            if s[i] != s[length - 1 - i]:
                return False

        return True
