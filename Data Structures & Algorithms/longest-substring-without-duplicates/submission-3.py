class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen : dict[str, int] = {}
        L, R = 0, 0
        max_length = 0
        
        # abba
        while R < len(s):
            if s[R] in seen:
                L = max(L, seen[s[R]] + 1) # L = 1
            seen[s[R]] = R # {'b' : 1}
            max_length = max(max_length, R - L + 1)
            R+=1
        return max_length