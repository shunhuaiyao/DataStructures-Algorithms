class Solution:
    def checkPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        isPalindrome = True
        for i in range(len(s)//2):
            if s[i] != s[-i-1]:
                isPalindrome = False
        return isPalindrome