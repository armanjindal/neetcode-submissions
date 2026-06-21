class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Create an array that maps 
        # Know they are equal length
        if len(s) != len(t):
            return False

        s_array = [0 for i in range(26)]
        
        # Count the number of timme each letter occurs
        # Store it in an array i.e 'a' maps to position -
        for i in range(len(s)):
            s_array[ord(s[i]) - ord('a')] += 1
            t_index = ord(t[i]) - ord('a')
            s_array[t_index] -= 1

        for value in s_array: 
            if value > 0:
                return False
        return True

        # Memory - O(n) (length of s)
        # Run time - O(n) - two for loops max duration 
        # Array look up is O(1)
        # Short Circuit - if the lengths are different then no need to compare
        # Edge Case - both empty -> for loops dont run --> return True

        