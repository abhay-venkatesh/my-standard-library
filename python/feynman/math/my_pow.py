class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        
        What does pow(x, n) do? It takes a number x, and then, 
        either multiplies x by itself n times, or divides x by itself n times,
        depending on the sign.
        
        Firstly, we can actually just multiply x by itself abs(n) times,
        and then if n is positive, return the value,
        or if it was negative, return the denominator. 
        
        We could recursively write, return x * myPow(x, n - 1),
        but that is not tail recursive, and neither does python support TRE 
        anyway. But it seems to be in the manageable python recursion range,
        so should be fine.
        
        Naive implementation:
        if n == 0:
            return 1
        elif n < 0:
            return 1 / (x * self.myPow(x, abs(n)-1))
        else:
            return x * self.myPow(x, n-1)
            
        But this cannot handle the massive tail depth. 
        Therefore, we need to iteratively implement it.
        
        Iterative implementation:
        accumulator = 1.0
        n_ = abs(n)
        while n_ > 0:
            accumulator *= x
            n_ -= 1
            
        if n < 0:
            return 1 / accumulator
        else:
            return accumulator
            
        But this times out on the input:
        0.00001
        2147483647
        
        Therefore, we need an efficient implementation.
        Squaring is easy with bit shifting. 
        """