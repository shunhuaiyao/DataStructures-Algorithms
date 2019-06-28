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

        """
        Time Complexity: O(N)
        numbers are stored in set to allow O(1) lookups -> check if num is "in" the set
        """
        numsSet = set(nums)
        lengthLongestNums = 0
        for num in numsSet:
            if num - 1 not in numsSet: # key condition -> find all unique consecutive sequence
                curNum = num
                tmplengthLongestNums = 1
                while curNum + 1 in numsSet:
                    curNum += 1
                    tmplengthLongestNums += 1
                lengthLongestNums = max(lengthLongestNums, tmplengthLongestNums)
        return lengthLongestNums

        """
        Time Complexity: O(NlogN)
        """
        # if len(nums) < 1:
        #     return 0
        # nums = sorted(nums)
        # print(nums)
        # lengthLongestNums = curLengthNum = 1
        # for i in range(len(nums)):
        #     if i+1 < len(nums) and nums[i] != nums[i+1]:
        #         if nums[i+1] == nums[i] + 1:
        #             curLengthNum += 1
        #         else:
        #             lengthLongestNums = max(lengthLongestNums, curLengthNum)
        #             curLengthNum = 1
        # return max(lengthLongestNums, curLengthNum)
