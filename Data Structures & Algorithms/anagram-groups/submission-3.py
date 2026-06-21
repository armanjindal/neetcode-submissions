from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Edge cases inputs - [], ["x"] --> [["x"]], [""] -> [[""]]

        # Algortithm
        # 1. Create a list with all the strings sorted
        # 2. Initialize a result_map -> sorted_string: list_number in result_list
        # 3. Iterate through sorted_array. 
        # 3A. If sorted_string not in result_map, create entry in result_list, update result_map
        # 3B. If sorted_string in result_map --> append original string to list in result_list list

        result_map : dict[str:int] = {}
        result_list : list[list[str]] = []

        for original_string in strs:
            sorted_string = "".join(sorted(original_string))
            if sorted_string not in result_map: # {"abc" : 0}
                result_list.append([original_string])
                result_map[sorted_string] = len(result_list) - 1
            else: # match against an existing anagram
                result_position = result_map[sorted_string]
                result_list[result_position].append(original_string)

        
        return result_list
            
                
