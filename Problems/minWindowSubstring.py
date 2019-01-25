from collections import Counter
class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        Given a string s and a string t,
        find the minimum window in s which will contain all the characters in t in complexity O(n).
        Example,
        Input: s = "ADOBECODEBANC", t = "ABC"
        Output: "BANC"
        """

        '''
        ans is a tuple structure where the length of the minimum window is stored as ans[0]
        and the start and end indices of chars are stored as ans[1] and ans[2].
        '''
        ans = float('inf'), None, None
        
        if not s or not t:
            return ""
        
        start = 0
        end = 0
        completed = 0
        '''
        Counter is a collection where elements are stored as dict keys 
        and their counts are stored as dict values.
        '''
        target_dict = Counter(t)
        needed = len(target_dict)
        windows_dict = dict()
        while end < len(s):
            char = s[end]
            windows_dict[char] = windows_dict.get(char, 0) + 1
            if char in target_dict and windows_dict[char] == target_dict[char]:
                completed += 1
            while start <= end and completed == needed:
                if end - start + 1 < ans[0]:
                    ans = end - start + 1, start, end
                char = s[start]
                windows_dict[char] = windows_dict.get(char, 0) - 1
                if char in target_dict and windows_dict[char] < target_dict[char]:
                    completed -= 1
                start += 1
            end += 1
        return '' if ans[0] == float('inf') else s[ans[1]:ans[2]+1]