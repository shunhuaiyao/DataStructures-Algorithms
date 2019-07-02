class Solution:

    def Fibonacci(self, k):
        # return the first k numbers of Fibonacci
        fibonacci = []
        i = 0
        while i <= k:
            if i == 0 or i == 1:
                fibonacci.append(i)
            else:
                fibonacci.append(fibonacci[i-2]+fibonacci[i-1])
            i += 1
        return fibonacci

    def nthOfFibonacci(self, n):
        """
        Sol 1:
        interative function
        """
        if n == 0 or n == 1:
            return n
        fibonacci = []
        fibonacci.append(0)
        fibonacci.append(1)
        i = 2
        while i <= n:
            fibonacci.append(fibonacci[i-2] + fibonacci[i-1])
            i += 1
        return fibonacci[n]
        """
        Sol 2:
        recursive function
        """
        if n == 0 or n == 1:
            return n
        return self.nthOfFibonacci(n-2) + self.nthOfFibonacci(n-1)