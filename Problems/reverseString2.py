class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        You need to reverse the first k characters for every 2k characters counting from the start of the string.
        If there are less than k characters left, reverse all of them.
        If there are less than 2k but greater than or equal to k characters,
        then reverse the first k characters and left the other as original.
        Example:
        Input: s = "abcdefg", k = 2
        Output: "bacdfeg"
        """
        if k == 0:
            return s
        
        i = 0
        reversedStr = ""
        while i < len(s):
            reversedStr += self.reverseAllChars(s[i:i+k]) + s[i+k:i+2*k]
            i += 2 * k
        return reversedStr
        
    def reverseAllChars(self, s):
        reversedStr = ""
        for char in s:
            reversedStr = char + reversedStr
        return reversedStr