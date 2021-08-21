class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        
        
        for substringSize in range(len(s), 0, -1):
            for i in range(len(s)):
                end = i + substringSize
                if end > len(s):
                    break
                else:
                    substring = s[i:end]
                    if substring[::-1] == substring:
                        return substring
                        
            
        
        return ""
            
            
            
        # brute force: start from beginning character and search for palindromes of length k, where k starts from length of the string
        # (sorted?) dict: key = character, value = list of indices the character appears -- grab the characters with the biggest gaps first
        