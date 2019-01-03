class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        Given a string which consists of lowercase or uppercase letters,
        find the length of the longest palindromes that can be built with those letters.
        Example,
        Given a string s = "abccccdd"
        return 7
        One longest palindrome "dccaccd" can be built from s.
        Assume the length of given string will not exceed 1,010.
        """

        count = 0
        hashTable = {}
        for char in s:
            if char not in hashTable.keys():
                hashTable[char] = 2
            else:
                count += hashTable.pop(char)
        if len(hashTable) != 0:
            count += 1
        return count