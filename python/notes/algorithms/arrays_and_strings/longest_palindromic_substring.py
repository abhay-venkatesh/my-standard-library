"""
longest_palindrome = "sas"
s = "sas"
table = [
    [True, False, True],
    [False, True, False],
    [False, False, True],
]

i = 0
j = 2
"""

def longest_palindrome(s):
    longest_palindrome = None 
    table = [[False for _ in range(len(s))] for _ in range(len(s))]
    for i in reversed(range(len(s)-1)):
        j = i
        while j < len(s):
            if s[i] == s[j] and (j - i < 3 or table[i+1][j-1]):
                table[i][j] = True
            
            if (table[i][j] and (not longest_palindrome or 
                                 j - i + 1 > len(longest_palindrome))):
                longest_palindrome = s[i:j+1]
            j += 1
    return longest_palindrome  

def main():
    print(longest_palindrome("sas"))

if __name__ == '__main__':
    main()