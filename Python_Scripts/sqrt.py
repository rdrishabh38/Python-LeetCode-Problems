"""Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
 

Constraints:

0 <= x <= 231 - 1
"""

#O(n)
def mySqrt(self, x):
    """
    :type x: int
    :rtype: int
    """
    i=0
    while((i*i)<=x):
        i+=1
    return i-1

#O(log(n)) optimized solution
def mySqrt(self, x):
    """
    :type x: int
    :rtype: int
    """
    if x in [0,1]:
        return x
    left=1
    right=x
    while(left<=right):
        mid=(left+right)//2
        sqr_mid=mid*mid
        if sqr_mid==x:
            return mid
        elif sqr_mid>x:
            right=mid-1
        else:
            left=mid+1
            
    return right