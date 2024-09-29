class Solution:
    def longestCommonSubsequence(self, text1, text2):
        m = len(text1)
        n = len(text2)

        # Create a 2D array (dp) initialized to 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Fill the dp array based on the recurrence relation
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]

# Example usage
solution = Solution()
text1 = "abcde"
text2 = "ace"
print(solution.longestCommonSubsequence(text1, text2))  # Output: 3
