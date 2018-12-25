import math
class Sorter:
    def mergeSort(self, nums):
        """
        Sorting a list of integer numbers in ascending order by merge sort
        :type nums: List[int]
        """
        if len(nums) > 1:
            mid = len(nums)//2
            lefSubNums = nums[:mid]
            rightSubNums = nums[mid:]
            leftSorter = Sorter()
            rightSorter = Sorter()
            leftSorter.mergeSort(lefSubNums)
            rightSorter.mergeSort(rightSubNums)
            self.conquer(nums, lefSubNums, rightSubNums)
    def conquer(self, nums, leftSubNums, rightSubNums):
        """
        Merging two sublist in ascending order into a list
        :type nums: List[int]
        :type leftSubNums: List[int]
        :type rightSubNums: List[int]
        """
        i = 0
        j = 0
        k = 0
        leftSubNums.append(math.inf)
        rightSubNums.append(math.inf)
        while k < len(nums):
            if leftSubNums[i] < rightSubNums[j]:
                nums[k] = leftSubNums[i]
                i += 1
            else:
                nums[k] = rightSubNums[j]
                j += 1
            k += 1
    def quickSort(self, nums):
        """
        Quick sort a list in ascending order
        :type nums: List[int]
        """
        self.quickSortHelpler(nums, 0, len(nums) - 1)
    def quickSortHelpler(self, nums, front, end):
        """
        :type nums: List[int]
        :type front: int
        :type end: int
        """
        if front < end:
            splitPoint = self.partition(nums, front, end)
            leftSorter = Sorter()
            rightSorter = Sorter()
            leftSorter.quickSortHelpler(nums, front, splitPoint - 1)
            rightSorter.quickSortHelpler(nums, splitPoint + 1, end)
    def partition(self, nums, front, end):
        """
        Sort a partition and return a split point
        :type nums: List[int]
        :type front: int
        :type end: int
        :rtype j: int
        """
        pivot = nums[front]
        i = front + 1
        j = end
        while i <= j:
            while i <= j and nums[i] <= pivot:
                i += 1
            while i <= j and nums[j] >= pivot:
                j -= 1
            if i <= j:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
        temp = nums[j]
        nums[j] = pivot
        nums[front] = temp
        return j
    