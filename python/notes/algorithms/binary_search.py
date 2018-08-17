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

A = [1, 1, 2, 3, 3, 4, 5, 5, 6]
i = binary_search(A, 3)
print(i)
i = binary_search(A, 12)
print(i)