class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        Given an array nums of n integers,
        find all unique triplets in the array which gives the sum of zero.
        Example,
        Given array nums = [-1, 0, 1, 2, -1, -4],
        A solution set is:
        [
            [-1, 0, 1],
            [-1, -1, 2]
        ]
        """
        triplets = list()
        if len(nums) < 3:
            return triplets
        nums = sorted(nums)
        fixedIndex = 0
        while fixedIndex < len(nums):
            fixed = nums[fixedIndex]
            complement = -1 * fixed
            frontIndex = fixedIndex + 1
            backIndex = len(nums) - 1
            while frontIndex < backIndex:
                if nums[frontIndex] + nums[backIndex] < complement:
                    frontIndex += 1
                elif nums[frontIndex] + nums[backIndex] > complement:
                    backIndex -= 1
                else:
                    front = nums[frontIndex]
                    back = nums[backIndex]
                    triplets.append([fixed, front, back])
                    while frontIndex < backIndex and back == nums[backIndex]:
                        backIndex -= 1
                    while frontIndex < backIndex and front == nums[frontIndex]:
                        frontIndex += 1
            fixedIndex += 1
            while fixedIndex < len(nums) and nums[fixedIndex] == fixed:
                fixedIndex += 1
        return triplets