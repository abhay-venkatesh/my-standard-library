class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        
        [
          [1,1,1],
          [1,0,1],
          [1,1,1]
        ]
        
        We need a way to set the row and column to 0 for each 0
        that was initially present in the matrix.
        
        If we set the row and column for each 0 in the matrix,
        then eventually the full matrix becomes 0, or something close
        to that since we do not really know whether each 0 was initially set,
        or set after encountering a specific 0 in the initial matrix.
        
        O(mn) solution is probably that we store an entire copy of the
        original matrix.
        
        We only really need to know if there was a 0 in a 
        specific row or column.
        That is the O(m + n) solution.
        
        An O(1) solution implies that the way we know 
        a 0 is originally set or not is not dependent on the problem size.
        
        Do we really need to remember the positions of the original 0s? 
        what if we do a two pass solution, where we set the original 0s
        to something else, a flag value, then modify the array,
        and then replace that something else back to 0s?
        
        Step 1:
        [
          [1,1,1],
          [1,inf,1],
          [1,1,1]
        ]
        
        Step 2:
        [
          [1,0,1],
          [0,inf,0],
          [1,0,1]
        ]
        
        Step 3:
        [
          [1,0,1],
          [0,0,0],
          [1,0,1]
        ]
        
        Again,
        
        Step 1:
        [
          [inf,1,2,inf],
          [3,4,5,2],
          [1,3,1,5]
        ]
        
        Step 2:
        [
          [inf,0,0,inf],
          [0,4,5,0],
          [0,3,1,0]
        ]
        
        Step 3:
        [
          [0,0,0,0],
          [0,4,5,0],
          [0,3,1,0]
        ]
        
        What is one issue with this approach?
        
        """
        