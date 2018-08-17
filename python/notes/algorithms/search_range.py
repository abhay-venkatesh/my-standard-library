def searchRange(A, target):
    i = 0
    j = len(A) - 1
    ret = [-1, -1]
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


