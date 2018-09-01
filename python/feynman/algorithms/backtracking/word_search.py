class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        visited = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
        return self.helper(board, word, visited, 0, 0)
        
        
    def helper(self, board, word, visited, i, j):
        if len(word) == 1 and board[i][j] == word:
            return True
        
        if i-1 >= 0 and not visited[i-1][j] and self.helper(board, word[1:], visited, i-1, j):
            return True