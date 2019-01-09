class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        Example,
        (i)
        nums1 = [1, 3]
        nums2 = [2]
        The median is 2.0
        (ii)
        nums1 = [1, 2]
        nums2 = [3, 4]
        The median is (2 + 3)/2 = 2.5
        """
        
        """
        Time complexity: O((m+n)log(m+n)),
        which m is the length of nums1 and n is the length of nums2.
        The time complexity of built-in sorted function in python is O(nlogn).
        
        nums = sorted(nums1 + nums2)
        if len(nums) % 2 == 0:
            median = (nums[int(len(nums)/2)-1] + nums[int(len(nums)/2)]) / 2
        else:
            median = nums[int(len(nums)/2)]
        return median
        """
        
        m = len(nums1)
        n = len(nums2)
        if m < n:
            nums1, nums2, m, n = nums2, nums1, n, m
        medianIndex = (m+n) // 2
        lastMedian = median = 0
        i = j = 0
        for k in range(medianIndex+1):
            lastMedian = median
            if i < m and j < n:
                if nums1[i] < nums2[j]:
                    i += 1
                    median = nums1[i-1]
                else:
                    j += 1
                    median = nums2[j-1]
            elif i < m:
                i += 1
                median = nums1[i-1]
            else:
                j += 1
                median = nums2[j-1]
        if (m+n) % 2 == 0:
            median = (lastMedian+median) / 2
        return median
            