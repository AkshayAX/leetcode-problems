#1143. Longest Common Subsequence

'''Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.'''


# solution 1
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # a c e
        #     0 0 0
        # a   1 1 1
        # b.  1 1 1
        # c   1 2 2
        # d.  1 2 2
        # e   1 2 3
        m = len(text1)
        n = len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i-1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        return dp[-1][-1]


# solution 2

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # a c e
        #     0 0 0
        # a   1 1 1
        # b.  1 1 1
        # c   1 2 2
        # d.  1 2 2
        # e   1 2 3
        # abcde;ace ->
        # a a  a c  a e
        # b a  b c  b e
        # c a  c c  c e
        # d a  d c  d e
        # e a  e c  e e
        # when a=a ; we add prevous val with 1; when point cc; then 1-> dp[i] = prev[i-1] + 1
        # else we take max(left,direct top); when point dc; then max(cc,da)
        # we need to track 2 rows here; becuase we're conisder top and left at the same time
        # max(dp[i-1],prev[i])

        m = len(text1)
        n = len(text2)
        dp = [0] * (m + 1)
        for i in range(n):
            prev = dp.copy()
            for j in range(1, m + 1):
                if text1[j - 1] == text2[i]:
                    dp[j] = prev[j-1] + 1
                else:
                    dp[j] = max(prev[j], dp[j - 1])
        return dp[-1]



