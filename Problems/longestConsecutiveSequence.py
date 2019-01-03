class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Given an unsorted list of integers,
        find the length of the longest consecutive elements sequence.
        Your algorithm should run in O(n) complexity.
        Example,
        Given a list nums = [100, 4, 200, 1, 3, 2]
        return 4
        One longest consecutive sequence is [1, 2, 3, 4], whose length is 4.
        """
        numsSet = set(nums)
        lengthLongestNums = 0
        for num in numsSet:
            if num - 1 not in numsSet:
                curNum = num
                tmplengthLongestNums = 1
                while curNum + 1 in numsSet:
                    curNum += 1
                    tmplengthLongestNums += 1
                lengthLongestNums = max(lengthLongestNums, tmplengthLongestNums)
        return lengthLongestNums