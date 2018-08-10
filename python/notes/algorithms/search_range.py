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

Example:
A = [1, 1, 1, 2, 2, 4, 4, 5]
target = 2

i = 3
j = 3
ret = (-1, -1)
mid = 2

"""
def searchRange(A, target):
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


