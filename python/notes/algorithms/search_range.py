"""
Given an input array, we want to search for a range of numbers that match
a target. 

We perform binary search to find this range. We are basically looking for
two numbers:
1. number that matches target but does not have the same number on the left
2. number that matches target but does not have the same number on the right 

But do we have to explicitly check that there is no same number on the left
or right? What if we keep moving in the leftward or rightward directions
until we no longer match?
"""

"""
Example:
A = [1, 1, 1, 2, 2, 4, 4, 5]
target = 2

i = 3
j = 3
ret = (-1, -1)
mid = 2
"""
def searchRange(A, target):
    """
    We begin with i = 0, j = len(A) - 1
    The loop terminates when i >= j, or more specifically,
    when i == j because mid would never return the number j itself,
    unless mid = 2*j, but that happens when i == j and the loop terminates
    when i == j.

    For our binary search routine, we have compare A[mid] to target,
    we will then have three possibilities:

    1. A[mid] < target, which means that target is in A[mid + 1:]
    2. A[mid] == target, which means that target is either at mid,
        or on the left of mid
    3. A[mid] > target, which means that the target is left of mid

    i, j is the range of interest, that is the range in which our target
    will be present. In arguing about the correctness of this piece of code,
    we want to understand how i, j move and when the loop ends.

    Imagine that we are searching on 
    [1, 1, 1, 2, 2, 4, 4, 5]
    [0, 1, 2, 3, 4, 5, 6, 7]

    with target = 2.

    We would find, possibly, the number 2 on index 4. We would then assign
    j to 4, and perhaps i = 2.

    By moving j towards the target, we force the mid to go leftwards,
    and we want to go as leftward as possible. 
    """
    i = 0
    j = len(A) - 1
    ret = (-1, -1)
    while i < j:
        mid = (i + j)//2
        if A[mid] < target:
            i = mid + 1
        else:
            j = mid

    if A[i] != target:
        return ret
    else: 
        ret[0] = i

    j = len(A) - 1
    while i < j:
        mid = ((i + j)//2) + 1
        if A[mid] > target:
            j = mid - 1
        else:
            i = mid
    ret[1] = j

    return ret


