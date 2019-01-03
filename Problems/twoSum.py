class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        Given a list of integers, 
        return indices of two numbers such that they add up to a specific target.
        Example, 
        Given nums = [2, 5, 3, 8], target = 11,
        return [2, 3]
        Assume that each input would have exactly one solution,
        and the same element may not be used twice.
        """
        
        """
        Sol 1:
        Two-pass hash table
        """
        hashTable = {}
        for index, num in enumerate(nums):
            hashTable[num] = index
        for index, num in enumerate(nums):
            complement = target - num
            if complement in hashTable.keys() and hashTable[complement] != index:
                return [index, hashTable[complement]]
        """
        Sol 2:
        One-pass hash table
        """
        hashTable = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in hashTable.keys():
                return [index, hashTable[complement]]
            hashTable[num] = index

