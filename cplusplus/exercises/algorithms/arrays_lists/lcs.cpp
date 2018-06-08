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

We begin by defining the ith prefix of X,Y,Z as Xi,Yi,Zi.
That is, if X = [ABCDE], then X2 = [AB] and X0 is the empty sequence.

Theorem: If X = [x1, x2, ..., xm] and Y = [y1, y2, ..., ym], and we let
Z = [z1, z2, ..., zk] be any LCS of X and Y, then we have
1. If xm = yn, then zk = xm = yn, and Zk-1 is an LCS of Xm-1 and Yn-1
2. If xm != yn, then zk != xm implies that Z is an LCS of Xm-1 and Y
3. If xm != yn, then zk != yn implies that Z is an LCS of X and Yn-1

Proof:
1. If zk != xm, then we could append xm = yn to Z to obtain a common
subsequence of X and Y of length k+1, contradicting the supposition that Z
is an LCS of X and Y.

For example, consider X = [1, 2, 3, 4, 5, 7] and
                      Y = [0, 2, 3, 4, 6, 7]

                Then, Z = [2, 3, 4]

We have xm = yn, but zk != xm. If we append xm = yn = 7 to Z, we obtain
a common subsequence of length k+1, which contradicts the supposition that Z
is the LCS of X and Y. Therefore, xm = ym implies zk = xm = yn.

Now, we also want to show that Zk-1 is an LCS of Xm-1 and Yn-1. Under the
assumption that Z is an LCS, Zk-1 has to at least be a common subsequence. It
has to also be the greatest possible one, otherwise Z could not be an LCS
of X and Y.

2. xm != yn, zk = yn, zk != xm.

For example, consider X = [1, 2, 3, 4, 5, 7] and
                      Y = [0, 2, 3, 4, 5]

                Then, Z = [2, 3, 4, 5]

Now, if Z were not an LCS of Xm-1 and Y, then that would contradict our LCS
assumption.

3. Symmetric to 2.

*/
