class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        text1 = s
        text2 = s[::-1]

        n = len(text1)
        m = len(text2)
        
        
        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i+1][j+1] +1
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        # print(dp)
        return dp[0][0]