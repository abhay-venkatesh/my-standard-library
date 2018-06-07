/*

--- The Longest Common Subsequence (LCS) Problem ---

A sequence X = [x1, x2, ..., xm] has a Subsequence Z = [z1, z2, ..., zk] if
there exists a strictly increasing sequence of indices [i1, i2, ..., ik], such
that for  all j = [1, 2, ..., k], we have xij = zj.

For two sequences X and Y, Z is a common subsequence if it is a subsequence
of both X and Y.

In the longest common subsequence problem, we have as

input: X = [x1, x2, ..., xm]
       Y = [y1, y2, ..., yn]

and we produce as

output: Z = [z1, z2, ..., zk]

that is the longest common subsequence of X and Y.

--- Characterizing the Optimal Substructure of LCS ---

Since each sequence of length n has 2^n subsequences, the brute force would
take O(2^n) tries.


*/
