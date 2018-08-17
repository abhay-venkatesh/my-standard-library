def binary_search(A, target):
    i = 0
    j = len(A) - 1
    while i < j:
        mid = (i + j)//2
        if A[mid] < target:
            i = mid + 1
        else:
            j = mid
    if A[i] != target: return -1
    return i

print(i)
i = binary_search(A, 12)
print(i)

"""
--- Binary Search ---
In order to analyze the correctness of this algorithm, we want to see
why doing this type of searching always works. 

For instance, if we do,
A = [1, 1, 2, 3, 3, 4, 5, 5, 6]
i = binary_search(A, 3)

The loop terminates when i == j, which happens because the search interval
keeps shrinking by half and eventually becomes size 2. When it is size 2,
then mid == i always, and then if we found our target, we will set
j = mid and terminate. If we didn't find our target, then we set j = mid 
or i = mid + 1, which forces termination regardless.

Basically, we define our loop invariant as: If our search target is present
in the array A, then it is in the subarray A[i:j+1]. 

At initialization this is trivially true. 
At maintainence, we have two possibilities, 
At termination, i == j,
therefore, the element of interest would be at A[i]. 

"""