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

        result_dictionary = defaultdict(list[str]) # {'abc' : ['abc', 'bac'], 'dae' : ['ade']}

        for original_string in strs:
            string_count: list[int] = [0 for _ in range (26)]
            for character in original_string:
                string_count[ord(character) - ord('a')] += 1

            result_dictionary[tuple(string_count)].append(original_string)


        return list(result_dictionary.values())
            
                
