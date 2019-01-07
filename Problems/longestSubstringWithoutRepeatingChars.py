class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        Given a string,
        find the length of the longest substring without repeating characters.
        Example, 
        (i) Given s = 'abcabcbb', return 3
        One ongest substring without repeating characters is 'abc'
        (ii) Given s = 'bbbbb', return 1
        One ongest substring without repeating characters is 'b'
        (iii) Given s = 'pwwkew', return 3
        One ongest substring without repeating characters is 'wke'
        (iv) Given s = 'abcadd', return 4
        One ongest substring without repeating characters is 'bcad'
        """
        charHash = dict()
        startIndex = lenLongestSubstring = 0
        for charIndex, char in enumerate(s):
            if char in charHash.keys():
                startIndex = max(startIndex, charHash[char] + 1)
            charHash[char] = charIndex
            lenLongestSubstring = max(lenLongestSubstring, charIndex - startIndex + 1)
        return lenLongestSubstring
