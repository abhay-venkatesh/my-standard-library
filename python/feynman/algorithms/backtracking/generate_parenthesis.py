class Solution:
    def generate_parenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        
        solutions = [
            ["()()"],
        ]

        --- stack = [], prefix = "", n = 2 ---
        --- stack = [")"], prefix = "(", n = 1 ---
        --- stack = ["))"], prefix = "((", n = 0 ---
        --- stack = [")"], prefix = "(()", n = 0 ---

        """
        solutions = []
        prefix = ""
        stack = []
        self.helper(stack, solutions, prefix, n)
        return solutions
        
    def helper(self, stack, solutions, prefix, n):
        if not stack and n == 0:
            solutions.append(prefix)
        else:
            stack_ = list(stack)
            if stack_:
                prefix_ = prefix + stack_.pop()
                self.helper(stack_, solutions, prefix_, n)
            
            stack_ = list(stack)
            if n > 0:
                prefix_ = prefix + "("
                stack_.append(")")
                self.helper(stack_, solutions, prefix_, n-1)

def main():
    s = Solution()
    print(s.generate_parenthesis(3))

if __name__ == '__main__':
    main()