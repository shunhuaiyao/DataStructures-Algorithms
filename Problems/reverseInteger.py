class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        Given a 32-bit signed integer, reverse digits of an integer.
        Only integers within the 32-bit signed integer range are allowed to store.
        Example,
        (i) 123, return 321
        (ii) 120, return 21
        (iii) -123, return -321
        """
        rev = ""
        strList = list(str(abs(x)))
        for char in strList:
            if rev != "" and len(rev) < len(str(pow(2, 31))) and int(char)*pow(10, len(rev)) >= pow(2, 31) - int(rev) :
                return 0
            rev = char + rev
        if x < 0:
            return int(rev) * -1
        return int(rev)