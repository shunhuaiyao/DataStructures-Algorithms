class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        Given a string s, find the longest palindromic substring in s.
        Example,
        (i) "babad", return "bab" or "aba"
        (ii) "cbbd", return "bb"
        """
        
        maxLen = startIndex = endIndex = 0
        for charIndex in range(len(s)):
            oddLen = self.expandFromCenter(s, charIndex, charIndex)
            evenLen = self.expandFromCenter(s, charIndex, charIndex+1)
            largerLen = max(oddLen, evenLen)
            if largerLen > maxLen:
                maxLen = largerLen
                startIndex = charIndex - (largerLen - 1) // 2
                endIndex = charIndex + largerLen // 2
        return s[startIndex:(endIndex+1)]
    
    def expandFromCenter(self, s, startIndex, endIndex):
        while startIndex >= 0 and endIndex < len(s) and s[startIndex] == s[endIndex]:
            startIndex -= 1
            endIndex += 1
        return endIndex - 1 - startIndex 