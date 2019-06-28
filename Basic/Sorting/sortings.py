import math
class Sorter:
    def mergeSort(self, nums):
        """
        Divide and Conquer
        Sorting a list of integer numbers in ascending order by merge sort
        :type nums: List[int]
        """
        if len(nums) > 1:
            mid = len(nums)//2
            leftSubNums = nums[:mid]
            rightSubNums = nums[mid:]
            self.mergeSort(leftSubNums)
            self.mergeSort(rightSubNums)
            self.conquer(nums, leftSubNums, rightSubNums)
    def conquer(self, nums, leftSubNums, rightSubNums):
        """
        Merging two sublist in ascending order into a list
        :type nums: List[int]
        :type leftSubNums: List[int]
        :type rightSubNums: List[int]
        """
        i = 0 # i is a indicator of leftSubNums
        j = 0 # j is an indicator of rightSubNums
        k = 0 # k is an indicator of nums
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
        Divide and Conquer
        Quick sort a list in ascending order
        :type nums: List[int]
        """
        self.quickSortHelpler(nums, 0, len(nums) - 1)
    def quickSortHelpler(self, nums, front, end):
        """
        partition 會把所有比splitPoint小的數放左邊，比splitPoint大的數放右邊
        :type nums: List[int]
        :type front: int
        :type end: int
        """
        if front < end:
            splitPoint = self.partition(nums, front, end)
            self.quickSortHelpler(nums, front, splitPoint - 1)
            self.quickSortHelpler(nums, splitPoint + 1, end)
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
    def insertionSort(self, nums):
        """
        在處理第i筆資料時，第1筆至第i−1筆資料必須先排好序。
        Sort a list by insertion sort
        :type nums: List[int]
        """
        if len(nums) > 1:
            for i in range(1, len(nums)):
                key = nums[i]
                j = i - 1
                while key < nums[j] and j >= 0:
                    nums[j+1] = nums[j]
                    j -= 1
                nums[j+1] = key
