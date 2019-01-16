class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        Given a string array,
        find the longest common prefix string amongst an array of strings.
        If there is no common prefix, return an empty string "".
        All given inputs are in lowercase letters a-z.
        Example,
        (i) Input: ["flower","flow","flight"], Output: "fl"
        (ii) Input: ["dog","racecar","car"], Output: ""
        """
        if len(strs) == 0:
            return ""
        commonPrefix = strs[0]
        for string in strs:
            while string.find(commonPrefix) != 0:
                commonPrefix = commonPrefix[:(len(commonPrefix)-1)]
                if len(commonPrefix) == 0:
                    return ""
        return commonPrefix