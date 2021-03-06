class Solution0:
    def increasing_triplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        
        Brute force:
        O(n^3) by checking all combinations
        
        --- O(n)-time, O(1)-space ---
        
        We use the following as code:
        Return true if there exists i, j, k 
        arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
        
        
        [1,9,8,7,5,4,3,6]
        i = 0, nums[i] = 1
        j = 6, nums[j] = 3
        k = 7, nums[k] = 6
        
        We want to find i,j,k such that
        arr[i] < arr[j] < arr[k]
        
        So, we just increment the index that does not fit,
        while ensuring that the index after it is greater than it        
        """
        if len(nums) < 3:
            return False
        
        i = 0
        j = 1
        k = 2
        while k < len(nums):
            if nums[i] < nums[j] < nums[k]:
                return True
            
            if nums[j] <= nums[i]:
                j += 1
                if j == k:
                    k += 1
            
            if nums[k] <= nums[j]:
                k += 1
        return False

class Solution1:
    def increasing_triplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        We want to find i,j,k such that
        arr[i] < arr[j] < arr[k]
        
        There are many possiblities if this is not true.
        That is a huge issue. We need to cover all those possibilities,
        and still successfully search.

        We cannot sort, or use any table. We need to algorithmically 
        look into this array in linear time.

        [1,9,8,7,5,4,3,6]
        i = 0, nums[i] = 1
        j = 1, nums[j] = 9
        k = 2, nums[k] = 8

        Perhaps we should think about this as fitting a frame.
        We need to figure out which number does not fit the frame,
        and fix that number.

        [4,3,2,9,6,7,4,1]
        i = 2, nums[i] = 2
        j = 3, nums[j] = 6
        k = 4, nums[k] = 7

        [1,10,5,2,8,3,6]

        if i does not fit,
        then increment all,
        if j does not fit, then increment j and k
        if k does not fit, then increment k

        [4,7,8,6,6,7,4,1]
        """

class Solution2:
    def increasing_triplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        
        Consider,
        nums = [x_0, ..., x_{n-1}]

        We are interested in checking if there are indexes 0 <= i < j < k <= n-1
        such that nums[i] < nums[j] < nums[k].

        We begin by letting i = 0, j = 1, k = 2. We want to be able to search
        all the indexes smartly, but not assuming any ordering on the nums. 

        if nums[i] < nums[j] < nums[k] holds true for i = 0, j = 1, k = 2,
        then we are done. Awesome. If not, then it is possible that:
        1. i does not fit
        2. j does not fit
        3. k does not fit

        or a combination of these don't fit. The thing is, the combinations
        are not all equal. I mean that if i does not fit, then we
        necessarily have to move i, j and k. If j does not fit, then we 
        necessarily have to move both j and k. If k does not fit,
        then we have to move k. These are all the possibilities. 

        Therefore, we have reduced the decision space that we have, at least
        at initialization. Does this hold true for any future states?

        Say we are at any 0 <= i < j < k <= n-1. If i does not fit,
        it is possible that nums[i+1] < nums[j] < nums[k] is the solution.
        But when would we be in such a situation? Let us construct an example.

        [8,8,8,8,4,6,7,7,7,7]
        [0,1,2,3,4,5,6,7,8,9]
        i = 3
        j = 5
        k = 7

        Is it even possible to have reached to this state with our current
        algorithm? Let us try:

        [8,8,8,8,4,6,7,7,7,7]
        [0,1,2,3,4,5,6,7,8,9]
        i = 4
        j = 5
        k = 6

        We never actually reach that state. This is because move our numbers
        as a sliding window until we reach a state in which we could
        possibly have a combination of i, j, k that satisfy our conditions.

        For us to reach the following state:
        [8,8,8,8,4,6,7,7,7,7]
        [0,1,2,3,4,5,6,7,8,9]
        i = 3
        j = 5
        k = 7

        We needed to have gone up to
        i = 3
        j = 4
        k = 5

        and then decided that j does not fit, but that would only happen if
        nums[i] < nums[k].
        """

class Solution3:
    def increasing_triplet(self, nums):
        """
        nums = [2,5,3,4,5]
        nums = [0,1,2,3,4]
        1,9,0
        i = 1
        j = 3
        k = 4

        """
        if len(nums) < 3:
            return False 
            
        i = 0
        j = 1
        k = 2
        while k < len(nums):
            if nums[i] < nums[j] < nums[k]:
                return True
            
            if nums[i] >= nums[k]:
                i += 1
                j += 1
                k += 1
            elif (nums[i] <= nums[j] >= nums[k] or 
                  nums[i] >= nums[j] <= nums[k]):
                j += 1
                k += 1
            else:
                k += 1

        return False

import sys

class Solution4:
    def increasing_triplet(self, nums):
        first, second = sys.maxsize, sys.maxsize
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False

def main():
    s = Solution4()
    testcases = [
        ([8,8,8,8,8,6,7,7,7,7], False),
        ([8,8,8,8,4,6,7,7,7,7], True),
        ([1,2,3,4,5], True),
        ([5,4,3,2,1], False),
        ([2,1,5,0,4,6], True),
        ([2,5,3,4,5], True),
        ([1,0,0,0,0,0,10,0,0,0,0,0,100], True)
    ]
    for testcase in testcases:
        nums = testcase[0]
        output = testcase[1]
        print(nums, output)
        assert s.increasing_triplet(nums) == output
        
    

if __name__ == '__main__':
    main()