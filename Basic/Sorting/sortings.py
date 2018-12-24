import math
class Sorter(object):
    def mergeSort(self, nums):
        """
        Sorting a list of integer numbers in ascending order by merge sort
        :type nums: List[int]
        """
        if len(nums)>1:
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
                

        