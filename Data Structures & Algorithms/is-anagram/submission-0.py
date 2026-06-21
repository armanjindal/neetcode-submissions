from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)

        for char_s in s: 
            s_dict[char_s] += 1
        
        for char_t in t:
            t_dict[char_t] += 1

        return s_dict == t_dict