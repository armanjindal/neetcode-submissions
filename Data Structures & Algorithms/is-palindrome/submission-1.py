import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', s)
        stripped_string = cleaned_text.lower().replace(" ", "")

        L, R = 0, len(stripped_string) - 1

        while L < R:
            if stripped_string[L] != stripped_string[R]:
                return False
            L += 1
            R -= 1
        return True 

        