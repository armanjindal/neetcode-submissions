class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) # maps from count array -> word
        for word in strs:
            character_counts = [0] * 26
            for char in word:
                character_counts[ord(char) - ord('a')] += 1
            
            result[tuple(character_counts)].append(word)
        
        return list(result.values())
                


        